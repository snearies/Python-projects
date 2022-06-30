import tweepy
import time
auth = tweepy.OAuthHandler('iL30G9NJpsINCedYTeppRtMR2', '4h2IUnVMc0eeZaJkY5D4ynmZxgWPvpcgEh2PEV4WsHnlkCJ7NV')
auth.set_access_token('1415181358385700875-g51sFNj5Yf2o7oorFAdD4OwYwY2RPK', 'ymQ0QXxwIQoDAZY8jwwkelyzhCQFcuFpj7m06z7p3ahxo')

api = tweepy.API(auth)

user = api.me()

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)

search_string = 'python'
numbersofTweets = 2

for tweet in tweepy.Cursor(api.search,search_string).items(numbersofTweets):
 try:
  tweet.favorite()
  print('I like that tweet')
 except tweepy.TweepError as e:
  print(e.reason)
 except StopIteration:
  break


#-------------------bot to follow people
#for follower in limit_handler(tweepy.Cursor(api.followers).items()):
# for follower in tweepy.Cursor(api.followers).items():
#  #print(follower.name)
#  if follower.name == ' ':
#   follower.follow()

