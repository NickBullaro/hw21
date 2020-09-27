# project1-nsb38
## This is a simple outline of my project using the Twitter API, spoonacular API, and flask.
Some of this README was taken from Professor Sresht's lecture 6 Heroku example README.

To use this code, you must follow these steps:
1. Sign up for the twitter developer portal at https://developer.twitter.com
2. Navigate to https://developer.twitter.com/en/portal/projects-and-apps and make a new app
3. Click on the key symbol after creating your project, and it will take you to your keys and tokens
    If needed, you can regenerate your access token and secret
4. Next, to install Tweepy, run the following in your terminal:
    sudo pip install tweepy
    (or) sudo pip3 install tweepy
    (or) pip install tweepy
    (or) pip3 install tweepy
5. Install flask using the same process as above ([sudo] pip[3] install flask)
6. Install spoonacular using the same process as above ([sudo] pip[3] install spoonacular)
7. Install python-dotenv using the same process as above ([sudo] pip[3] install python-dotenv)
8. Navigtate to spoonacular.com/food-api
9. Create an account and save your api key
10. Clone this repository by using git clone https://github.com/NJIT-CS490/project1-nsb38
11. Add all of your keys (from steps 3 & 9) by making a new root-level file called keys.env and populating it as follows:
    export SPOON_KEY=''
    export CONSUMER_KEY=''
    export CONSUMER_KEY_SECRET=''
    export ACCESS_TOKEN=''
    export ACCESS_TOKEN_SECRET=''
12. Run `main.py`
13. If on Cloud9, preview running application.
14. Sign up for heroku at heroku.com 
15. Install heroku by running npm install -g heroku
16. Go through the following steps:
    heroku login -i
    heroku create
    git push heroku master
17. Navigate to your newly-created heroku site!
18. Add your secret keys (from keys.env) by going to https://dashboard.heroku.com/apps
    and clicking into your app. Click on Settings, then scroll to "Config Vars." Click
    "Reveal Config Vars" and add the key value pairs for each variable in user_tweets.py
    Your config var key names should be:
    SPOON_KEY
    KEY
    KEY_SECRET
    TOKEN
    TOKEN_SECRET
19. Configure requirements.txt with all requirements needed to run your app.
20. Configure Procfile with the command needed to run your app.
21. If you are still having issues, you may use heroku logs --tail to see what's wrong.


### Known Problem & Additional Feature
1. My only known problem is sometimes when fetching a tweet containing the selected keyword, the keyword is found in the tweet's author rather than the content. In an attempt to avoid this, I created an IF statement that only passed the tweet if the keyword was in the content. This sometimes causes errors, so in the future, I will either figure out a way to ensure a tweet with the keyword in the content is fetched, or I will simply fetch more tweets to decrease the chance of it causing an error.
2. One additional feature I would add would be to include the actual recipe instructions to the web page. The spoonacular API has a "Analyze Recipe Instructions" endpoint that would allow me to fetch the list of instructions for the selected recipe. I would implement this just like I did with the list of ingredients. In main.py, I would run the .get, parse the .json() for each individual step, add them to each a list as a different element, pass the list using Flask, then print out the list in my .html file. I would of course have to "beautify" the page using CSS as well.


### Technical Issues
1. One technical issue I faced was having the list of ingredients appear over the picture. I was able to edit the HTML code so that the words were not over the picture, but the list numbers were still causing problems. Because I made the picture float left, I decided to make the list of ingredients float right, and it worked.
2. Another issue I was facing was how to use the spoonacular API to get all of the information I needed. Running a complex search didn't give me all of the information needed, so I scowered through the spoonacular API documentation. After searching, I decided to run the complex search for the recipe ID, then used the ID to run a get on the recipe information, which gave me everything else I needed. Then it became all about parsing the resulting .json() to get each individual attribute I needed.
3. One more issue I faced was setting up the .html and .css files. For me, this was the hardest part of the project. Working the HTML and CSS code to properly set up the page and get each element to be in their needed spot was difficult. For example, getting the tweet box to be under both the picture and list of ingredients. After a lot of google searches, I found https://primestudyhub.blogspot.com/css-boxes which helped me figure out how to create my boxes, as well as format them well with all of the other elements around it.
