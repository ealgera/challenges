import csv
from collections import Counter

fpath = r"./movie_metadata.csv"
min_movies = 4

def readCSV():
    ''' Lees bestand en maak per regel een dictionary met de velden:
            director_name, movie_title, title_year, imdb_score
        Verwijder lege regels en films ouder dan 1961
        Geef een lijst terug met al deze dictionaries (l).
    '''
    l = []
    with open(fpath) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=",")
        for row in csv_reader:
            if len(row["director_name"]) > 0 and len(row["title_year"]) > 0:
                d = {}
                if  int(row["title_year"]) > 1960:
                    d["director_name"] = row["director_name"]
                    #d["movie_title"] = row["movie_title"]
                    d["titles"].append(row["movie_title"])
                    d["title_year"] = row["title_year"]
                    d["imdb_score"] = row["imdb_score"]
                    l.append(d)
    return l

def countMovies(l):
    ''' Tel de films per 'director' 
        Maak een dictionairy met per 'director' het aantal gemaakte films
        Neem alleen directors op die een minimaal aantal films hebben geregiseerd
    '''
    d = {}
    for item in l:
        if item["director_name"] not in d:  # Tel de films per director
            d[item["director_name"]] = 0        
        d[item["director_name"]] += 1
    t = {k:[v] for k,v in d.items() if v > min_movies} # Alleen directors met minimaal aantal films
    return t


def main():
    dictList = readCSV()

    print(dictList)
    #movies_per_director = countMovies(dictList)
    #print(len(movies_per_director), movies_per_director)


if __name__ == "__main__":
    main()