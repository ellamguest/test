# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 10:53:45 2015

@author: emg
"""

from film_data_dicts import director_films, writer_films, ratings_list,\
 film_directors, film_writers

def get_film_info(film):
    '''get the film's [rating, director, writer]'''
    rating = ratings_list[film]
    director = film_directors[film]
    writer = film_writers[film]
    return [rating, director, writer]


def print_film_info(film):
    info = get_film_info(film)
    print 'Film: {}'.format(film)
    print 'Rating: {}'.format(info[0])
    print 'Director(s): {}'.format(info[0])
    print 'Writers(s): {}'.format(info[0])

def get_director_ratings(director):
    ratings = []    
    films = director_films[director] #is this the right format?
    for film in films:
        rating = ratings_list[film]
        info = [film, rating]
        ratings.append(info)
    return ratings