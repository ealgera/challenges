from string import ascii_lowercase
import sys
import os

from movies import get_movie as get_word  # keep interface generic
from graphics import hang_graphics

ASCII = list(ascii_lowercase)
HANG_GRAPHICS = list(hang_graphics()) # 07 Plaatjes
ALLOWED_GUESSES = len(HANG_GRAPHICS)  # = 7
PLACEHOLDER = '_'


class Hangman(object):
    def __init__(self, _w):
        self.word = _w
        self.letters_found = []
        self.word_sofar = [PLACEHOLDER if i != " " else " " for i in _w]
        self.letters_guessed = []
        self.guesses = 1
        self.false_guesses = 0
        self.score = 0

    def print_word_sofar(self):
        for letter in self.word_sofar:
            print(letter, end="")
        print()
        print(self.word)
    
    def print_header(self):
        os.system('clear')
        print(HANG_GRAPHICS[self.false_guesses])
        print()
        print(f"Guess number   : {self.guesses}. \t\tScore: {self.score}")
        print(f"False guesses  : {self.false_guesses}")
        print(f"Guessed letters: {self.letters_guessed}")
        print()
        print()

    def check_letter(self, _l):
        self.guesses += 1
        self.letters_guessed.append(_l)
        if _l in self.word:
            self.letters_found.append(_l)
            self.score += 2
            tmp = [i for i, letter in enumerate(self.word) if letter.lower() == _l.lower()]
            for i in range(len(tmp)):
                self.word_sofar[tmp[i]] = _l
        else:
            self.false_guesses +=1

# or use functions ...

if __name__ == '__main__':
    if len(sys.argv) > 1:
        word = sys.argv[1]
    else:
        word = get_word()
    
# init / call progra
hm = Hangman(word)
playing = True
#os.system('clear')

while playing:
    if hm.false_guesses > ALLOWED_GUESSES:
        playing = False
        break
    hm.print_header()
    hm.print_word_sofar()
    my_letter = input("What letter do you want? ")
    hm.check_letter(my_letter)

# Game Over...
print()
print(" >>> GAME OVER <<<")
print()