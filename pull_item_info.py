# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 15:35:47 2015

@author: emg
"""

from read_film_files import ratings_list
from film_data_dump import director_films, writer_films


def search_filmographies(film, d):
    '''search director_films or writer_films for all
    directors or writers of a film'''
    results = []    
    for x in d:
        if film in d[x]:
            results.append(x)
    return results

def get_film_info(film):
    '''get the film's [rating, director, writer]'''
    rating = ratings_list[film]
    director = search_filmographies(film, director_films)
    writer = search_filmographies(film, writer_films)
    info = [rating, director, writer]
    return info

def print_film_info(film):
    '''print the film's info'''
    info = get_film_info(film)
    print 'Film: {}'.format(film)
    print 'Rating: {}'.format(info[0])
    print 'Director(s): {}'.format(info[0])
    print 'Writers(s): {}'.format(info[0])

def get_artist_ratings(name, filmography_dict):
    '''get the ratings for every film by the writer of director
    filmography_dict = director_films or writer_films'''
    ratings = []    
    films = filmography_dict[name] #is this the right format?
    for film in films:
        rating = ratings_list[film]
        info = [film, rating]
        ratings.append(info)
    return ratings