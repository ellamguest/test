# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 15:35:47 2015

@author: emg
"""

from film_data_dicts import ratings_list, film_directors, film_writers

#make hash table of indexes? set()?

def get_film_info(film):
    '''get the film's [rating, director, writer]'''
    rating = ratings_list[film]
    director = film_directors[film]
    writer = film_writers[film]
    return [rating, director, writer]

def print_film_info(film):
    '''print the film's info'''
    info = get_film_info(film)
    print 'Film: {}'.format(film)
    print 'Rating: {}'.format(info[0])
    print 'Director(s): {}'.format(info[1])
    print 'Writers(s): {}'.format(info[2])

def get_ratings(name, filmography_dict):
    '''get the ratings for every film by the writer of director
    filmography_dict = director_films or writer_films'''
    ratings = []    
    films = filmography_dict[name] #is this the right format?
    for film in films:
        if film in set(ratings_list):
            rating = ratings_list[film]
        else:
            rating = 'n/a' # why ratings not be found?
        ratings.append([film, rating])
    return ratings

def print_ratings(name, filmography_dict):
    '''print the ratings for every film by the writer of director
    filmography_dict = director_films or writer_films'''
    ratings = get_ratings(name, filmography_dict)
    s = 0
    n = len(ratings)
    print name
    print '-----------------------'
    for x in ratings:
        print '{}: {}'.format(x[1], x[0])
        if x[1] == 'n/a':
            n -= 1
        else:
            s += float(x[1])
    print '-----------------------'
    print '{:.2f} : Average Rating'.format(s/n)
        