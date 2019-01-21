from data import DICTIONARY, LETTER_SCORES
import string

def load_words():
    """Load dictionary into a list and return list"""
    l = []
    with open(DICTIONARY, "rt") as f:
        l=[line.rstrip('\n') for line in f]
    return l

def calc_word_value(w):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    som = 0
    q = list(w)
    for i in q:
        if (i in string.ascii_lowercase) or (i in string.ascii_uppercase):
            som += LETTER_SCORES[i.upper()]
    return som

def max_word_value(l=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    max_value = 0
    max_word = '' 
    word_count = 0
    if l == None:
        print("Inlezen dictionary bestand...")
        l = load_words()
    print("Aantal woorden ingelezen: {}".format(len(l)))
    for i in l:
        word_count += 1
        s = calc_word_value(i)
        if s > max_value:
            max_value = s
            max_word = i
    
    print("Woord: {}, max-waarde   : {}".format(max_word, max_value))
    print("Aantal woorden gechecked: {}".format(word_count))

    

if __name__ == "__main__":
    # run unittests to validate
    t = ['bob', 'JuliaN', 'PyBites', 'benzalphenylhydrazone']
    max_word_value()
