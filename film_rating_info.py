# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 10:23:38 2015

@author: emg
"""

import scipy as sp
from film_data_dicts import director_films, writer_films, ratings_list
from pull_item_info import get_ratings
from tools import check_in_dict

# is this the best way to create dicts w/ ratings?
def add_ratings(filmography_dict):
    for name, films in filmography_dict.iteritems():
        new = []
        nums = []
        for film in films:
            if str(film) in set(ratings_list):
                rating = ratings_list[film]
            else:
                rating = sp.nan
                new.append([film, rating])
            nums.append(rating)
        new.append(['Average Rating', sp.nanmean(nums)])
        filmography_dict[name] = new
    return filmography_dict

def avg_rating(name, filmography_dict):
    ''''returns avg rating of a writer or director'''
    ratings = get_ratings(name, filmography_dict)
    avg = ratings[-1][1]
    return avg

# REPLACCE WITH DICTS W/ RATINGS    

def get_director_avg_rating(name):
    d_name = check_in_dict(name, director_films)
    n = d_name[0]
    avg = avg_rating(n, director_films)
    return avg

def get_writer_avg_rating(name):
    w_name = check_in_dict(name, writer_films)
    n = w_name[0]
    avg = avg_rating(n, writer_films)
    return avg

def get_all_avg_ratings(name):
    d_avg = get_director_avg_rating(name)
    w_avg = get_writer_avg_rating(name)
    return d_avg, w_avg

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
        