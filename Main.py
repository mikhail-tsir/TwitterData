import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob

consumer_key = 'elSaHjf5iVQcWZcSxBJkmTpc8'
consumer_secret = 'JPG3dy1nvBZmvU8JrPFimbpa7gIjoMHrDwQzGXkhjjmIUF2PG8'
access_token = '1192235837003579392-DGyix5A2s1vlnUq01bfK0GPSu2Zife'
access_token_secret = '8WyxFl3Yr1ms1fIAjajMDiaKrT9FtDZBbPbMUQAUTDsjw'

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


def get_tweet_sentiment(tweet):
    '''
    Utility function to classify sentiment of passed tweet
    using textblob's sentiment method
    '''
    # create TextBlob object of passed tweet text
    # analysis = TextBlob(clean_tweet(tweet))
    analysis = TextBlob(tweet)
    # set sentiment
    return analysis.sentiment
    # return analysis.sentiment.polarity


def get_tweets(query, count=300):
    '''
    Main function to fetch tweets and parse them.
    '''
    # empty list to store parsed tweets
    tweets = []
    average_sentiment = 0
    num = 0

    try:
        # call twitter api to fetch tweets
        fetched_tweets = api.search(q=query, count=count)
        num = len(fetched_tweets)
        print("length", num)
        # parsing tweets one by one
        for tweet in fetched_tweets:
            # empty dictionary to store required params of a tweet
            parsed_tweet = {}
            # saving text of tweet
            parsed_tweet['text'] = clean_tweet(tweet.text)
            # saving sentiment of tweet
            parsed_tweet['sentiment'] = get_tweet_sentiment(tweet.text)
            sent = get_tweet_sentiment(tweet.text)
            average_sentiment += sent * 100
            print(sent * 100)
            parsed_tweet['retweets'] = tweet.retweet_count
            # appending parsed tweet to tweets list
            if tweet.retweet_count > 0:
                # if tweet has retweets, ensure that it is appended only once
                if parsed_tweet not in tweets:
                    tweets.append(parsed_tweet)
            else:
                tweets.append(parsed_tweet)

                # return parsed tweets
        return (average_sentiment / num)

    except tweepy.TweepError as e:
        # print error (if any)
        print("Error : " + str(e))


def get_tweet_sentiments(query):
    return (get_tweets(query.upper()) + get_tweets(query.capitalize()) + get_tweets(query.lower()))/3


print(get_tweet_sentiment("I knew that Trump fit the stereotypical profile of all cult leaders, which is essentially malignant narcissism, which is the narcissism – plus the psychopathic elements of feeling above the law, the pathological lying, paranoia, jealousy, the harassment."))
