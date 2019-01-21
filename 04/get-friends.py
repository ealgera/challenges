from collections import namedtuple
from  datetime import datetime
import csv
import os

import tweepy

from config import CONSUMER_KEY, CONSUMER_SECRET
from config import ACCESS_TOKEN, ACCESS_SECRET

DEST_DIR = 'data'
EXT = 'csv'
NUM_TWEETS = 1

TweetData = namedtuple('TweetData', 'id_str created_at text')
TweetUser = namedtuple('TweetUser', 'id_str name screen_name')


class UserTweets(object):
    """
    """
    #tweets = []
    
    def __init__(self, _twitter_id):
        self.tweets = []
        self.friends = []
        self._auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        self._auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        self._api = tweepy.API(self._auth)

        self._id = _twitter_id
        self._screen_name = "@" + _twitter_id

        self.friends = self._get_friends()
        #self.tweets = self._get_tweets()
        #self._save_tweets()

    def _get_tweets(self):
        twitter_data = self._api.user_timeline(screen_name=self._screen_name, count=NUM_TWEETS)
        return [TweetData(t.id_str, t.created_at, t.text.replace('\n','')) for t in twitter_data]

    def _get_friends(self):
        ids = []
        for page in tweepy.Cursor(self._api.friends, screen_name=self._screen_name).pages():
            for user in page:
                ids.append(TweetUser(user.id_str, user.name, user.screen_name))
        return ids

    def _print_tweets(self):
        for t in self.tweets:
            print(t)
            print()
    
    def __getitem__(self, position):
        return self.tweets[position]

    def __len__(self):
        return len(self.tweets)

    def _save_tweets(self):
        _path = os.getcwd()
        _fname = self._id + "." + EXT
        os.chdir(_path + "/" + DEST_DIR)

        with open(_fname, "w") as f:
            f_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
            f_writer.writerow(TweetData._fields)
            f_writer.writerows(self.tweets)                
        os.chdir(_path)


if __name__ == "__main__":

    handle = 'ericalgera'
    print('--- {} ---'.format(handle))
    user = UserTweets(handle)
    for idx, val in enumerate(user.friends):
        friend_id, friend_name, friend_screen_name = user.friends[idx]
        print()
        print('*** {}'.format(friend_name))
        friends_data = user._api.user_timeline(id=friend_id, count=NUM_TWEETS)
        friend_tweets = [TweetData(t.id_str, t.created_at, t.text.replace('\n','')) for t in friends_data]
        if len(friend_tweets) > 0:
            for t in friend_tweets:
                #if ("Python" in t.text) or ("python" in t.text):
                tweet_date = t.created_at   # "2017-07-27 17:59:15" 
                #tweet_date = datetime.strptime(tweet_date_str, '%Y-%m-%d %H:%M:%S')
                delta = datetime.now() - tweet_date
                if delta.days > 183:
                    print(".......>>>>>>> {} - {}".format(t.created_at, t.text))
        else:
            print('*** {} Heeft geen Tweets...'.format(friend_name))

