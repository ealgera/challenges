class UserTweet:

    def __init__(self, n, sn, t):
        self.name = n
        self.screenname = sn
        self.tweet = t
        #self.tweet_parsed = []

    def print_Tweet(self):
        print(f"Naam  : {self.name}")
        print(f"Screen: {self.screenname}")
        print(f"Tweet : {self.tweet}")
