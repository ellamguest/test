# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 17:55:11 2015

@author: emg
"""
import pdb
import re
import cPickle
import file_parsers.py as fp

ratings_file = 'ratings.list'
writers_file = 'writers.list'
directors_file = 'directors.list'


###################################################################################
#CREATE LINES VARAIBLES + DUMP INFO
###################################################################################



film_ratings = read_ratings(ratings_file)
writer_lines = get_writer_lines(writers_file)
director_lines = get_director_lines(directors_file)

###################################################################################
#DUMP INFO
###################################################################################

def save_film_names():
    film_names = read_films(ratings_file)
    cPickle.dump(film_names, open('film_list.pickle', 'w+'))
    
def load_film_list():    
    return cPickle.load(open('film_list.pickle', 'r'))

#film_list = load_film_list() if 'film_list' not in dir() else film_list ------------ test these 1 at a time

def save_film_ratings():
    film_ratings = read_ratings(ratings_file)
    cPickle.dump(film_ratings, open('film_ratings_list.pickle', 'w+'))

def load_ratings_list():    
    return cPickle.load(open('film_ratings_list.pickle', 'r'))

#ratings_list = load_ratings_list() if 'ratings_list' not in dir() else ratings_list

def save_writer_films():
    writer_lines = get_writer_lines(writers_file)
    writer_films = pull_items(writer_lines)
    cPickle.dump(writer_films, open('writer_films.pickle', 'w+'))
    
def load_writer_films():    
    return cPickle.load(open('writer_films.pickle', 'r'))

#writer_films = load_writer_films() if 'writer_films' not in dir() else writer_films

def save_director_films():
    director_lines = get_director_lines(directors_file)
    director_films = pull_items(director_lines)
    cPickle.dump(director_films, open('director_films.pickle', 'w+'))
    
def load_director_films():    
    return cPickle.load(open('director_films.pickle', 'r'))

#director_films = load_director_films() if 'director_films' not in dir() else director_films


################################################################################
## IF I WANT A FULL COPY OF FILM : INFO?!?!
################################################################################
#def make_film_dict(film_list):
#    d = {}
#    for film in film_list:
#        info = get_film_info(film)
#        if info[1] != [] and info[2] != []:
#            print film, info
#            d[film] = info
#    return d

#def save_film_dict():
#    film_dict = make_film_dict(film_list)
#    cPickle.dump(film_dict, open('film_dict.pickle', 'w+'))
#    
#def load_film_dict():    
#    return cPickle.load(open('film_dict.pickle', 'r'))


#save_film_dict()
#film_dict = load_film_dict if 'film_dict' not in dir() else film_dict

#d = make_film_dict(film_names) ----------- test last
#
#for x in d:
#    print x
#    print d[x]
#    print ''