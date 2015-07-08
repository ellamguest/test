# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 15:35:47 2015

@author: emg
"""

import scipy as sp
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

def check_in_dict(name, d):
    return [n for n in d if name in n.lower()]

def get_ratings(name, filmography_dict):
    '''get the ratings for every film by the writer of director
    filmography_dict = director_films or writer_films'''
    ratings = []
    nums = []
    films = filmography_dict[name] #is this the right format?
    for film in films:
        if film in set(ratings_list):
            rating = float(ratings_list[film])
        else:
            rating = sp.nan # why ratings not be found?
        ratings.append([film, rating])
        nums.append(rating)
    ratings.append(['Average Rating', sp.nanmean(nums)])
    return ratings

def avg_rating(name, filmography_dict):
    ''''returns avg rating of a writer or director'''
    ratings = get_ratings(name, filmography_dict)
    avg = ratings[-1][1]
    return avg

def get_director_avg_rating(name):
    d_name = check_in_dict(name, director_films)
    n = d_name[0]
    avg = avg_rating(n, director_films)
    return n, avg

def get_writer_avg_rating(name):
    w_name = check_in_dict(name, writer_films)
    n = w_name[0]
    avg = avg_rating(n, writer_films)
    return n, avg


get_avg_d_rating('whedon, joss')
Out[221]: ('Whedon, Joss', 7.8250000000000002)

get_avg_d_rating('whedon, joss')

def avg_rating_dict(filmography_dict):
    ''''makes a dict of writer/director : avg rating'''
    d = {}
    for name in filmography_dict:
        ratings = get_ratings(name)
        d[name] = ratings[-1][1]
    return d

def print_ratings(name, filmography_dict):
    '''print the ratings for every film by the writer of director
    filmography_dict = director_films or writer_films'''
    ratings = get_ratings(name, filmography_dict)
    print name
    print '-----------------------'
    for name, rating in ratings[0:-1]:
        print '{}: {}'.format(rating, name)
    print '-----------------------'
    print '{}: {}'.format(ratings[-1][1], ratings[-1][0])
        