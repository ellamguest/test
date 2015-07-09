# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 09:46:32 2015

@author: emg
"""

from film_data_dicts import film_directors, film_writers
from pull_item_info import get_director_avg_rating, get_writer_avg_rating
from top_250_test import top_250_films

top_10_films = top_250_films[0:10]

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