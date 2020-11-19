import sys
import os
import random
from os.path import join, dirname
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
import spoonacular as sp
import requests
import flask
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), 'keys.env')
load_dotenv(dotenv_path)

spoon_key = os.environ['SPOON_KEY']
consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth_api = API(auth)





#Flask----------------
app = flask.Flask(__name__)
@app.route('/')
def index():
    keyword_list = ["pasta", "pizza", "soup", "cake", "cookies",
        "rice", "steak", "chicken", "ham", "kebab", "egg", "bagel"]
    num = random.randint(0, 11)

    #Twitter--------------
    search_query = keyword_list[num] + " -filter:links"

    tweets = Cursor(auth_api.search, q=search_query, lang="en").items(1)
    try:
        for tweet in tweets:
            tweety = "'{}' -@{} {}".format(tweet.text, tweet.user.screen_name, tweet.created_at)
            print(tweety)
    except StopIteration:
        tweety = "No tweet was found related to the selected keyword!"

    #Spoonacular-------------

    url1 = "https://api.spoonacular.com/recipes/complexSearch?apiKey="
    url2 = "&query="
    url3 = "&number=1"
    url = url1 + str(spoon_key) + url2 + keyword_list[num] + url3
    response = requests.get(url)
    respo = response.json()
    recipe_id = respo['results'][0]['id']
    information_url = "https://api.spoonacular.com/recipes/"
    url = information_url + str(recipe_id) + "/information?apiKey=" + str(spoon_key)
    respons = requests.get(url)
    res = respons.json()

    title = res['title']
    link = res['image']
    source_link = res['sourceUrl']
    serving_size = res['servings']
    total_time = res['readyInMinutes']
    ingred = []
    ingredient_amounts = []

    for i in range(len(res['extendedIngredients'])):
        ingred.append(res['extendedIngredients'][i]['name'])
        ingredient_amounts.append(str(res['extendedIngredients'][i]['measures']['us']['amount'])
            + " " + res['extendedIngredients'][i]['measures']['us']['unitShort'])


    return flask.render_template(
        "index.html",
        ftweet = tweety,
        tit=title,
        lin=link,
        sourc=source_link,
        servin=serving_size,
        minutes=total_time,
        len = len(ingred),
        ingred=ingred,
        ingredAmount = ingredient_amounts
        )


app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
)
