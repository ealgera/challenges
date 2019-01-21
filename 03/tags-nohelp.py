from bs4 import BeautifulSoup
from difflib import SequenceMatcher

TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87


def get_tags():
    """Find all tags in RSS_FEED.
    Replace dash with whitespace."""
    with open('rss.xml','rt') as f:
        soup = BeautifulSoup(f,'html.parser')

    categories = []
    for item in soup.find_all('item'):
        for category in item.find_all("category"):
            categories.append(category.text)

    return categories 


def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags"""
    mydict = dict()

    for item in tags:
        if item not in mydict:
            mydict[item] = 0
        else:
            mydict[item] += 1

    mydict_top = {k: mydict[k] for k in list(mydict)[:TOP_NUMBER]}

    mydict_top_sorted = sorted(mydict_top.items(), key=lambda kv: kv[1], reverse=True)

    return mydict_top_sorted

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR"""
    sim_list = []
    for i in range(len(tags)):
        for j in range(len(tags)):
            a = tags[i]
            b = tags[j]
            if (a != b) and (a[0] == b[0]):    
                score = (similar(a, b))
                if score > SIMILAR:
                    tup = (a, b)
                    sim_list.append(tup)
    return sim_list



if __name__ == "__main__":
    tags = get_tags()
    top_tags = get_top_tags(tags)
    print('* Top {} tags:'.format(TOP_NUMBER))
    for tag, count in top_tags:
        print('{:<20} {}'.format(tag, count))
    similar_tags = dict(get_similarities(tags))
    print()
    print('* Similar tags:')
    for singular, plural in similar_tags.items():
        print('{:<20} {}'.format(singular, plural))
