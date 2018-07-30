#import the required libraries
import tweepy
import json
import textblob
from textblob import TextBlob
import paralleldots
import nltk
from nltk.corpus import stopwords
from collections import Counter
nltk.download('stopwords')

#Authentication with Twitter
consumer_key = "DfMujCmTUqG4eoLzPaHGPYvjm"
consumer_secret = "1PQh4jqIpjTQFuj52TZUEb66LxTtgirA8vbpJoefnD5jGxGB06"
access_token = "1017780532044877824-kzMUFs9RhvCoDqJ492Tjt3wcSt9Lnb"
access_secret = "PnU6TmqdgLE1qj2yYZpkwiA8vJ74fanEXx4n7rVjG360f"
oauth = tweepy.OAuthHandler(consumer_key, consumer_secret)
oauth.set_access_token(access_token, access_secret)
api = tweepy.API(oauth)

#choice for users to choose the function they wish to perform

f1=True
def choice():
    global f1
    
    while f1==True:
        
        print("User menu")
        print("1. Retrieve tweets from twitter")
        print("2. Count the followers")
        print("3. Sentiment of the tweet")
        print("4. Location of tweet")
        print("5. Compare the tweets")
        print("6. Analyse the top usage")
        print("7. Tweet a message")
        print("8. Exit")
        choice_input = int(input("What do you wanna do?"))
        if choice_input==1:
            Search()
            choice()
        elif choice_input==2:
            count_followers()
            choice()
        elif choice_input==3:
            sentimentAnalysis()
            choice()
        elif choice_input==4:    
               location_tweet()
               choice()
        elif choice_input==5:
             compare()
             choice()
        elif choice_input==6:
            topUsage()
            choice()
        elif choice_input==7:
            tweetMessage()
            choice()
        elif choice_input==8:
            print("Exit")
            f1=False
            choice()

        else:
            print("Sorry invalid fucntion")
            choice()
             
#query for twitter bot
def query():
    global tweets
    t_input=input("enter hashtag for which you want to retrieve tweets:")
    tweets=api.search(q=t_input)
    
#retrieve tweets
def Search():
    query()
    status=tweets[0]
    json_str=json.dumps(status._json,indent=5,sort_keys= True)
    print(json_str)



#count followers
def count_followers():
    query()
    print("UserName      Follower Count")
    for tweet in tweets:
          print(tweet.user.name+" " +str(tweet.user.followers_count))

#determine sentiments

def sentimentAnalysis():
    positive_sentiment=0;
    negative_sentiment=0;
   
    
    query()
    from paralleldots import set_api_key, get_api_key,sentiment
    
    set_api_key("8dyQhJPFerUALsn2lBpMAftocXOIr6bAFb6vJcrEYYM")
    get_api_key()
    for tweet in tweets:
        txt = tweet.text
        sentiment_value = sentiment(txt)
        value = sentiment_value['sentiment']
        if value == "positive":
            positive_sentiment = positive_sentiment + 1
            
        else:
            negative_sentiment = negative_sentiment + 1
        
    if positive_sentiment > negative_sentiment :
        print("Sentiment is Positive ")
    
    else:
        print("Sentiment is Negative")
    
    
#tweets based on location
def location_tweet():
    global loc,lang,time_zone1
    
    query()
    location = {}
    language = {}
    time_zone = {}
    for tweet in tweets:
        loc = tweet.user.location
        lang = tweet.user.lang
        time_zone1 = tweet.user.time_zone
        if loc in location:
            location[loc] += 1
        else:
            location[loc] = 1
        if lang in language:
            language[lang] += 1
        else:
            language[lang] = 1
        if time_zone1 in time_zone:
            time_zone[time_zone1] += 1
        else:
            time_zone[time_zone1] = 1
        language_count = dict(Counter(language).most_common(5))
    print("Language:")
    print(language_count)
    location_count = dict(Counter(location).most_common(5))
    print("Location:")
    print(location_count)
    time_zone_count = dict(Counter(time_zone).most_common(5))
    print("Time Zone:")
    print(time_zone_count)

        


#compare tweets
def compare():
    tweet1 = 0
    tweet2 = 0
    # for narendra modi
    tweets = api.user_timeline(screen_name="narendramodi", count=200, tweet_mode="extended")
    for compare_tweet in tweets:
        fulltext = compare_tweet.full_text
        tmp = []
        tmp.append(fulltext)
        temp = tmp
        import re
        data = re.sub(r"http\S+", "", str(temp))
        data= re.split(r"\s", data)
        for word in data:
            word=word.upper()
            if word == "AMERICA" or word == "US" or word=="USA" or word=="UNITED STATES OF AMERICA":
                tweet1 = tweet1 + 1
    print("USA BY NARENDRA MODI: "+ str(tweet1))

    # for donald trump
    tweets = api.user_timeline(screen_name="realDonaldTrump", count=200, tweet_mode="extended")
    for compare_tweet in tweets:
        fulltext = compare_tweet.full_text
        tmp = []
        tmp.append(fulltext)
        temp = tmp
        import re
        data = re.sub(r"http\S+", "", str(temp))
        data = re.split(r"\s", data)
        for word in data:
            word = word.upper()
            if word == "INDIA" or word == "India" or word == "India":
                tweet2 = tweet2 + 1
    print("INDIA BY DONALD TRUMP: " + str(tweet2))

 
#top usage     
def topUsage():
  
    global count
    stop_words = set(stopwords.words('english'))
    x = [x.upper() for x in stop_words]
    tweets = api.user_timeline(screen_name="msdhoni", count=200, tweet_mode="extended")
    for tweet_compare in tweets:
        fulltext = tweet_compare.full_text
        tmp = []
        tmp.append(fulltext)
        temp = tmp
        import re
        cur_tweet = re.sub(r"http\S+", "", str(temp))
        cur_tweet1 = re.split(r"\s", cur_tweet)
        cur_tweet = [w for w in cur_tweet1 if not w in stop_words]
        cur_tweet=[]
        for w in cur_tweet1:
            if w not in stop_words:
                cur_tweet.append(w)
                count = Counter(cur_tweet).most_common(10)
        print(count)    
#post a tweet
def tweetMessage():
    msg=input("what tweet you want to post?")
    api.update_status(msg)


choice()

