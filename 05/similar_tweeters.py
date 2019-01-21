import sys
import re
from usertweets import UserTweets
import nltk
from nltk.corpus import stopwords
from collections import Counter
from gensim import corpora, models, similarities


def similar_tweeters(user1, user2):
    u1 = UserTweets(user1)
    u2 = UserTweets(user2)
    
    clean_tweats(u1)
    clean_tweats(u2)

    dict_u1 = corpora.Dictionary(u1.tweets_new)
    dict_u2 = corpora.Dictionary(u2.tweets_new)
    corpus_u1 = [dict_u1.doc2bow(text) for text in u1.tweets_new]
    corpus_u2 = [dict_u2.doc2bow(text) for text in u2.tweets_new]
    #print(corpus_u1)
    lsi = models.LsiModel(corpus_u1, id2word=dict_u1, num_topics=3)
    for wordlist in u2.tweets_new:
        vec_bow = dict_u1.doc2bow(wordlist)
        print(f"In de zin: {wordlist} is de verdeling:")
        for w in vec_bow:
            #print(f"\t{dict_u1[w[0]]} komt {w[1]} keer voor.")
            
            vec_lsi = lsi[vec_bow] # convert the query to LSI space
            print(vec_lsi)


def clean_tweats(u):
    text_tokenize(u)
    text_remove_words(u)
    text_remove_stopwords(u)
    text_remove_single_words(u)
    text_remove_empty_lists(u)

def text_remove_empty_lists(u):
    tmp = []
    for wordlist in u.tweets_new:
        #for word in wordlist:
        if len(wordlist) > 0:
            tmp.append(wordlist)
    u.tweets_new = tmp

def text_remove_single_words(u):
    tmp = []
    for wordlist in u.tweets_new:
        for word in wordlist:
            tmp.append(word)
    t = Counter(tmp)  # Dict met woorden en aantal voorkomens over n Tweets
    tmpwrdlist = []
    for wordlist in u.tweets_new:
        tmplst = []
        for word in wordlist:
            if t[word] > 1:
                tmplst.append(word)
        tmpwrdlist.append(tmplst)
    u.tweets_new = tmpwrdlist
        
def text_remove_words(u):
    charlist = ['@','#', 'http', 'text', '&', ':', '-', '…', '...', '0','1','2','3','4','5','6','7','8','9']
    tmpwrdlist = []
    for wordlist in u.tweets_new:
        tmplst = []
        for word in wordlist:
           if not any(x in word for x in charlist):
               if len(word) > 2:
                   tmplst.append(word)
        tmpwrdlist.append(tmplst)
    u.tweets_new = tmpwrdlist

def text_tokenize(u):
    for id, dt, txt in u.tweets:
        u.tweets_new.append(txt.split())

def text_remove_token(u, t):
    tweets_tmp = []
    for wordlist in u.tweets_new:
        tmp = [s for s in wordlist if t not in s]
        tweets_tmp.append(tmp)
    u.tweets_new = tweets_tmp

def text_remove_stopwords(u):
    nltk.download('stopwords')
    tweets_tmp = []
    for wordlist in u.tweets_new:
        tmp = [word for word in wordlist if word not in stopwords.words('english')]
        tweets_tmp.append(tmp)
    u.tweets_new = tweets_tmp
    

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('Usage: {} <user1> <user2>'.format(sys.argv[0]))
        sys.exit(1)

    user1, user2 = sys.argv[1:3]
    similar_tweeters(user1, user2)
