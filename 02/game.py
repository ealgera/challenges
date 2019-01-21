#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

from data import DICTIONARY, LETTER_SCORES, POUCH
import string
from itertools import permutations
import random

NUM_LETTERS = 7

# re-use from challenge 01
def calc_word_value(w):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    #return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)
    som = 0
    q = list(w)
    for i in q:
        if (i in string.ascii_lowercase) or (i in string.ascii_uppercase):
            som += LETTER_SCORES[i.upper()]
    return som

# re-use from challenge 01
def max_word_value(l=None):
    """Calc the max value of a collection of words"""
    #return max(words, key=calc_word_value)
    max_value = 0
    max_word = '' 
    word_count = 0
    if l == None:
        print("Inlezen dictionary bestand...")
        l = DICTIONARY  #load_words()
    print("Aantal woorden ingelezen: {}".format(len(l)))
    for i in l:
        word_count += 1
        s = calc_word_value(i)
        if s > max_value:
            print("Woord gevonden! {}".format(i))
            max_value = s
            max_word = i
    
    print("Woord: {}, max-waarde   : {}".format(max_word, max_value))
    print("Aantal woorden gechecked: {}".format(word_count))

def calc_perm(l):
    t = []
    for i in range(len(l)):
        t.append(list(permutations(l, r=i+1)))
    return t

def check_list(l):
    tmp=[]
    for i in range(len(l)):
        for j in range(len(l[i])):
            k = l[i][j]
            w = ''.join(k)
            tmp.append(w)
    return tmp

def main():
    #t = ['bob', 'JuliaN', 'PyBites', 'ben'] #zalphenylhydrazone']
    #max_word_value()
    
    # Trek random letters uit de POUCH
    letter_list = [POUCH[random.randint(1, 98)] for _ in range(5)]
    perm_words = calc_perm(letter_list)
    found_word_list = check_list(perm_words)

    max_word_value(found_word_list)

    #print(found_word_list)

    #for perm in perm_letters:
    #    tmp = ''.join(perm)
    #max_word_value(list(perm_letters))

    #str1 = ''.join(letters)
    #print(str1)
    # Bereken alle permutaties van de getrokken letters
    # Bereken het woord met de grootste waarde
    # Laat de letters aan de speler zien
    # Vraag de speler om het woord met de grootste waarde
    # Laat het woord met de grootste waarde zien en bereken de score van de speler

if __name__ == "__main__":
    main()
