import re
import tweepy
from tweepy import OAuthHandler
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import json
import gensim
from gensim.summarization import keywords

consumer_key = 'XXXXXX'
consumer_secret = 'XXXXXX'
access_token = 'XXXXXX'
access_token_secret = 'XXXXXX'

try:
    # create OAuthHandler object
    auth = OAuthHandler(consumer_key, consumer_secret)
    # set access token and secret
    auth.set_access_token(access_token, access_token_secret)
    # create tweepy API object to fetch tweets
    api = tweepy.API(auth)
except:
    print("Error: Authentication Failed")


def clean_tweet(tweet):
    '''
    Utility function to clean tweet text by removing links, special characters
    using simple regex statements.
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])| (\w+:\ / \ / \S+)", " ", tweet).split())


# def get_tweet_sentiment(tweet):
#     '''
#     Utility function to classify sentiment of passed tweet
#     using textblob's sentiment method
#     '''
#     # create TextBlob object of passed tweet text
#     # analysis = TextBlob(clean_tweet(tweet))
#     analysis = TextBlob(tweet)
#     # set sentiment
#     return analysis.sentiment
#     # return analysis.sentiment.polarity


def get_tweet_sentiment(sentence):
    sentiment = SentimentIntensityAnalyzer()
    score = sentiment.polarity_scores(sentence)
    return score['compound']


pos_tweets = []
neg_tweets = []


def get_tweets(query, c=99):
    '''
    Main function to fetch tweets and parse them.
    '''
    # empty list to store parsed tweets
    tweets = []
    average_sentiment = 0
    num = 0

    allpos = ""
    allneg = ""

    try:
        # call twitter api to fetch tweets
        print("-------- QUERY ------")
        print(query)
        fetched_tweets = api.search(q=query, count=c)
        # parsing tweets one by one
        for tweet in fetched_tweets:
            # empty dictionary to store required params of a tweet
            parsed_tweet = {}
            # saving text of tweet
            parsed_tweet['text'] = clean_tweet(tweet.text)
            # saving sentiment of tweet
            sent = get_tweet_sentiment(tweet.text)
            if sent > 0:
                allpos += clean_tweet(tweet.text) + " "
            else:
                allneg += clean_tweet(tweet.text) + " "

            average_sentiment += sent
            num += 1
        poswords = keywords(allpos,words = 10,scores = False, lemmatize = True, split=True)
        negwords = keywords(allneg,words = 10,scores = False, lemmatize = True, split=True)
        poswords2 = [i for i in poswords if len(i) > 3 and i != 'https']
        negwords2 = [i for i in negwords if len(i) > 3 and i != 'https']
       # print(poswords2)
        #print(negwords2)
        print("-------------")
        print(json.dumps({'avg_sentiment': str(average_sentiment / num),
                           'pos_keywords': poswords2,
                           'neg_keywords': negwords2}))
        return json.dumps({'avg_sentiment': str(average_sentiment / num),
                           'pos_keywords': poswords2,
                           'neg_keywords': negwords2})

    except:
        # print error (if any)
        print("Error : " + str(e))
        return json.dumps({'avg_sentiment': "N/A",
                           'pos_keywords': "N/A",
                           'neg_keywords': "N/A"})
