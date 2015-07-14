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

def films_info_dict(films):
    '''make a dict of film : [ratings, director, writer] for films in list'''
    d = {}
    for film in films:
        d[film] = get_film_info(film)
    return d

def get_ratings(name, filmography_dict):
    '''get the ratings for every film by the writer of director
    filmography_dict = director_films or writer_films'''
    ratings = []
    nums = []
    films = filmography_dict[name]
    for film in films:
        if film in set(ratings_list):
            rating = float(ratings_list[film])
        else:
            rating = sp.nan # figure out why some ratings not found
        ratings.append([film, rating])
        nums.append(rating)
    ratings.append(['Average Rating', sp.nanmean(nums)])
    return ratings


