# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 09:46:32 2015

@author: emg
"""

import scipy as sp
from line_processing import *
from film_data_dicts import ratings_list, film_directors, film_writers,\
 films_info_dict, director_films, writer_films
from pull_item_info import get_film_info, get_director_avg_rating, get_writer_avg_rating
from top_250_test import top_250_films

top_10_films = top_250_films[0:10]

top_10_films_info = films_info_dict(top_10_films)

top_10_directors = []

for film in top_10_films:
    d = film_directors[film]
    for v in d:
        if v not in top_10_directors:
            top_10_directors.append(v)
        
top_10_director_ratings_dict = {}

for name in top_10_directors:
    print 'Getting rating for ', name
    rating = get_director_avg_rating(name)
    top_10_director_ratings_dict[name] = [str(rating)]

top_10_directors_ranked = []

for k, v in top_10_director_ratings_dict.iteritems():
    top_10_directors_ranked.append([v, k])

top_10_directors_ranked.sort(reverse=True)

top_10_director_films = {}

for director in top_10_directors:
    films = director_films[director]
    top_10_director_films[director] = films


top_10_writers = []

for film in top_10_films:
    w = film_writers[film]
    for v in w:
        if v not in top_10_writers:
            top_10_writers.append(v)
        
top_10_writer_ratings_dict = {}

for name in top_10_writers:
    print 'Getting rating for ', name
    rating = get_writer_avg_rating(name)
    top_10_writer_ratings_dict[name] = [str(rating)]

top_10_writers_ranked = []

for k, v in top_10_writer_ratings_dict.iteritems():
    top_10_writers_ranked.append([v, k])

top_10_writers_ranked.sort(reverse=True)

top_10_writer_films = {}

for writer in top_10_writers:
    films = writer_films[writer]
    top_10_writer_films[writer] = films

#adding ratings
def add_ratings(filmography_dict):
    for name, films in filmography_dict.iteritems():
        new = []
        for film in films:
            if str(film) in set(ratings_list):
                rating = ratings_list[film]
            else:
                rating = sp.nan
                new.append([film, rating])
        filmography_dict[name] = new
    return filmography_dict




def pull_item_info(data):
    print 'Formatting lines...'
    lines = format_lines(data)
    regex = re.compile(pattern)
    results = {}
    n = 0
    while n < len(lines):
        line = lines[n]
#        print n, line
        if re.search(pattern, line[0]) == None:
            name = line[0]
            item = line[1]
        else:
            item = line[0]
        item = regex.findall(item)[0]
        n += 1
        rating = ratings_list[item]
        if name in results:
            results[name].append(item)
        else:
            results[name] = [item, rating]
        if n%100000 == 0:
            print n, line
    return results