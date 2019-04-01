"""
Turn the following unix pipeline into Python code using generators

$ for i in ../*/*py; do grep ^import $i|sed 's/import //g' ; done | sort | uniq -c | sort -nr
   4 unittest
   4 sys
   3 re
   3 csv
   2 tweepy
   2 random
   2 os
   2 json
   2 itertools
   1 time
   1 datetime
"""
from pathlib import Path
import re
from collections import defaultdict

def gen_files(pat):
# Generator. Levert steeds (per keer) een filehandle naar python bestanden in path 'pat'.
    path = Path(pat).rglob('*.py')
    for filename in path:
        print("->", filename)
        yield open(filename, 'rt')

def gen_lines(files):
# Generator. Levert steeds (per keer) een regel uit 'file'
    for file in files:
        yield from file

def gen_grep(lines, pattern):
# Generator (zie 'haakjes' in return). Levert per keer een regel met het gevonden 'pattern'.
    patc = re.compile(pattern)
    #for line in lines:
    #    if patc.search(line):
    #        print(f"----> *{line.rsplit()[-1]}*")
    return (line.rsplit()[-1] for line in lines if patc.search(line))

def gen_count(lines):
    d = defaultdict(int)
    for l in lines:
        print(f"----> {l}")
        d[l] += 1
    #d2 = dict((item, word.count(item)) for item in set(word))
    return sorted(d.items(), key=lambda x: x[1])  # Sorteer op 'value'.

if __name__ == "__main__":
    search_pat = r"^import\s"
    path = '/home/eric/Programming/Python/PyBites/mychallenges'
    files = gen_files(path)    # Per keer een 'open' bestand in het opgegeven pad.
    lines = gen_lines(files)   # Per keer een regel uit een bestand.
    greplines = gen_grep(lines, search_pat) # Per keer een regel waarin het patroon voorkomt.
    the_count = gen_count(greplines)  # start de 'loop' zodat de gen_ functies waardes teruggeven.
    for k, v in the_count:
        print(f"{k} - {v}")