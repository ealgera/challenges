import json
from usertweet import UserTweet
from pprint import pprint
from textblob import TextBlob
 
def parse(s):
    alfa_list = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
    not_alfa = list("#@&;…") 
    word_list = s.split(" ")
    t = []
    for word in word_list:
        if (any (x in word for x in alfa_list)) and not (any (x in word for x in not_alfa)):
            # Alleen woorden met alfanumerieke letters. Geen woorden met niet-alfanumerieke letters.
            t.append(word)
    return t

with open('data/stream_Brexit.json', 'r') as f:
    user_tweets = []
    for line in f:
        tweet = json.loads(line)
        ut = UserTweet(parse(tweet['user']['name']), parse(tweet['user']['screen_name']), parse(tweet['text']))
        user_tweets.append(ut)

positive, totaal = 0, 0
for tweet in user_tweets:
    totaal += 1
    t = ' '.join(tweet.tweet)
    sent = TextBlob(t)
    if sent.sentiment[0] > 0.5:
        positive += 1
        print(f"{totaal:04} -- {sent.sentiment[0]:6.3f} - {t}")

print()
print(f"Aantal positieve tweets: {positive} (van totaal {totaal} tweets).")

