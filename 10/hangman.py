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

    def print_word_sofar(self):
        for letter in self.word_sofar:
            print(letter, end="")
        print()
        for i in range(len(self.word_sofar)):
            print(i%10, end="")
        print()
        print()
        print(self.word)


# or use functions ...

if __name__ == '__main__':
    if len(sys.argv) > 1:
        word = sys.argv[1]
    else:
        word = get_word()
    
# init / call progra
hm = Hangman(word)
playing = True
os.system('cls')

while playing:

    hm.print_word_sofar()

# Game Over...