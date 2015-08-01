# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 09:46:32 2015

@author: emg
"""

import scipy as sp
import itertools
from line_processing import *
from film_data_dicts import ratings_list, film_directors, film_writers,\
 films_info_dict, director_films, writer_films
from pull_item_info import get_film_info, get_director_avg_rating,\
 get_writer_avg_rating, get_ratings
from top_250_test import top_250_films

top_10_films = top_250_films[0:10]

top_10_films_info = films_info_dict(top_10_films)

def top_10_directors():
    nested_directors = [v[1] for _, v in top_10_films_info.iteritems()]
    top_10_directors = list(itertools.chain(*nested_directors))
    return top_10_directors

top_10_directors = top_10_directors()
        
top_10_directors_ratings_dict = {}
for x in top_10_directors:
    top_10_director_ratings_dict[x] = get_ratings(x, director_films)

rank = []
for k, v in top_10_directors_ratings_dict.iteritems():
    rank.append([v[-1][1], k])
rank.sort(reverse=True)
    


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

