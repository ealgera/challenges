import csv
from collections import defaultdict, namedtuple
from operator import attrgetter

MOVIE_DATA = 'movie_metadata.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960
MAX_MOVIES = 20

Movie = namedtuple('Movie', 'title year score')

def get_movies_by_director():
    '''Extracts all movies from csv and stores them in a dictionary
    where keys are directors, and values is a list of movies (named tuples)'''
    d = defaultdict(list)
    with open(MOVIE_DATA) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=",")
        for row in csv_reader:
            if len(row["director_name"]) > 0 and len(row["title_year"]) > 0:
                if  int(row["title_year"]) >= MIN_YEAR:
                    m = Movie(title=row["movie_title"], year=row["title_year"], score=row["imdb_score"])
                    if m not in d[row["director_name"]]:
                        d[row["director_name"]].append(m)
    return d

def get_average_scores(directors):
    '''Filter directors with < MIN_MOVIES and calculate averge score'''
    t = {k:v for (k,v) in directors.items() if len(v) >= MIN_MOVIES}
    for d, ml in t.items():
        mean = _calc_mean(ml)
        t[d].append(mean)
    return t

def _calc_mean(movies):
    '''Helper method to calculate mean of list of Movie namedtuples'''
    s = 0
    for m in movies:
        s += float(m.score)
    return (round((s / len(movies)),1))

def print_results(directors):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''
    sorted_directors = sorted(directors.items(), key = lambda kv:(kv[1][-1], kv[0]), reverse=True)
    
    sep_line = '-' * 60
    dir_counter = 1
    
    for director, movies in sorted_directors[:MAX_MOVIES]:
        print(f'{str(dir_counter).zfill(2)}. {director:<52} {movies[-1]}')
        dir_counter += 1
        print(sep_line)

        for m in sorted(movies[:-1], key=attrgetter('score'), reverse=True):
            print(f'{m.year}] {m.title:<50} {m.score}')
        print()

def main():
    '''This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py'''
    directors = get_movies_by_director()
    directors = get_average_scores(directors)
    print_results(directors)

if __name__ == '__main__':
    main()
