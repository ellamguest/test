# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 11:28:47 2015

@author: emg
"""


def add_avg_rating(name, d):
    ratings = []
    for v in d[name]:
        ratings.append(float(v[1]))
    return sp.nanmean(ratings)

def make_directors_info_dict(film_info_d):
    d = {}
    for k, v in film_info_d.iteritems():
        info = (k, v[0], v[2])
        if len(v[1]) == 1:
            name = v[1][0]
        else:
            names = v[1]
            for x in names: #need to fix multiple director entries
                d[x] = [info]
        if name in set(d):
            d[name].append(info)
        else:
            d[name] = [info]
    for k, v in d.iteritems():
        avg = add_avg_rating(k, d)
        v.append(avg)
    return d
    


    

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