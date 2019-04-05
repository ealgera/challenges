from collections import namedtuple
import csv
import os

import tweepy

from config import CONSUMER_KEY, CONSUMER_SECRET
from config import ACCESS_TOKEN, ACCESS_SECRET

DEST_DIR = 'data'
EXT = 'csv'
NUM_TWEETS = 100

TweetData = namedtuple('TweetData', 'id_str created_at text')


class UserTweets(object):
    """TODOs:
    - create a tweepy api interface
    - get all tweets for passed in handle
    - optionally get up until 'max_id' tweet id
    - save tweets to csv file in data/ subdirectory
    - implement len() an getitem() magic (dunder) methods"""

    #tweets = []
    
    def __init__(self, _twitter_id):
        self.tweets = []
        self.tweets_new = []
        self._auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        self._auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

        self._id = _twitter_id
        self._api = tweepy.API(self._auth)

        self._screen_name = "@" + _twitter_id

        #self.tweets = self._get_tweets()
        self.tweets = self._getcsv_tweets()
        #self._save_tweets()

    def _getcsv_tweets(self):
        _fname = self._id + "." + EXT
        with open(_fname, "r") as f:
            f_reader = csv.reader(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
            my_list = list(f_reader)
        return my_list

    def _get_tweets(self):
        twitter_data = self._api.user_timeline(screen_name=self._screen_name, count=NUM_TWEETS)
        return [TweetData(t.id_str, t.created_at, t.text.replace('\n','')) for t in twitter_data]

    def _print_tweets(self):
        print(f"Tweets van: {self._id}. Aantal tweets is {len(self.tweets)-1}.")
        print()
        for t in self.tweets:
            print(t)

    def _print_tweets_new(self):
        print(f"Tweets van: {self._id}. Aantal tweets is {len(self.tweets_new)-1}.")
        print()
        for t in self.tweets_new:
            print(f"{len(t)} - {t}")
    
    def __getitem__(self, position):
        return self.tweets[position]

    def __len__(self):
        return len(self.tweets)

    def _save_tweets(self):
        #_path = os.getcwd()
        _fname = self._id + "." + EXT
        #os.chdir(_path + "/" + DEST_DIR)

        with open(_fname, "w") as f:
            f_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
            f_writer.writerow(TweetData._fields)
            f_writer.writerows(self.tweets)               
        #os.chdir(_path)


if __name__ == "__main__":

    for handle in ('pybites', 'evanderburg', 'ericalgera'):
        print('--- {} ---'.format(handle))
        user = UserTweets(handle)
        for tw in user[:5]:
            print("***: {} - {}".format(tw.id_str, tw.created_at))
        print(len(user))
        #print(user.tweets)

