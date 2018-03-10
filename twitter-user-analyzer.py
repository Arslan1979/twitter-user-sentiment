from textblob import TextBlob
import tweepy
import sys

## authenticating with Twitter

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# user
screen_name = str(sys.argv[1])
print('Reading ' + str(screen_name) + ' ..')

# overall sentiment variable
sentiment = 0

tweets = []

# iterate through all tweets in screen_name timeline
tweet_count = 0
for tweet in tweepy.Cursor(api.user_timeline, screen_name=screen_name).items():
    tweets.append(tweet.text)
    tweet_analysis = TextBlob(tweet.text)
    sentiment += tweet_analysis.sentiment.polarity 
    tweet_count += 1
    if tweet_count % 1000 == 0:
        print('Analyzing tweets..')

print('Analyzed a total of: ' + str(tweet_count) + ' tweets.')
print('Users overall sentiment: ' + str(sentiment))
print('Average sentiment per tweet: ' + str(sentiment/len(tweets)))
