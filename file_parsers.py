# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 12:14:04 2015

@author: emg
"""
import pdb
import re
import cPickle

writers_file = 'writers.list'
directors_file = 'directors.list'
ratings_file = 'ratings.list'



###################################################################################
#BREAK FILES INTO LINES
###################################################################################

def read_films(filename, header=281407, footer=633534):
    results = []
    for i, line in enumerate(open(filename)):
        if header < i <= footer:          
            result = line.split('  ')[-1].strip()
            results.append(result)
            print i, 'film', result

    return results

def read_ratings(filename, header=281407, footer=633534):
    results = {}
    for i, line in enumerate(open(filename)):
        if header < i <= footer:       
            name = line.split('  ')[-1].strip()
            rating = line.split('  ')[-2].strip()
            print i, 'rating', rating, name
            results[name] = [rating]

    return results
    
#previous footer=3582903
def get_writer_lines(filename, header=301, footer=4101660):
    results = []
    for i, line in enumerate(open(filename)):
        if header < i <= footer:        
#            print i, 'writer', line
            results.append(line)
    return results

#previous footer=2244913

def get_director_lines(filename, header=234, footer=2639293):
    results = []
    for i, line in enumerate(open(filename)):
        if header < i <= footer:
            print i, 'director', line
            results.append(line)
    return results

###################################################################################
#BREAK LINES INTO ITEMS
###################################################################################

 

###################################################################################
#COLLATE INFO INTO DICT
###################################################################################

def search_filmographies(film, d):
    results = []    
    for x in d:
        if film in d[x]:
            results.append(x)
    return results

def get_film_info(film):
    rating = ratings_list[film]
    director = search_filmographies(film, director_films)
    writer = search_filmographies(film, writer_films)
    info = [rating, director, writer]
    return info

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




