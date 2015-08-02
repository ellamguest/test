# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 15:18:13 2015

@author: emg
"""

import cPickle
from read_film_files import read_films, ratings_file, read_ratings, get_writer_lines,\
writers_file, get_director_lines, directors_file
from line_processing import pull_items



def save_film_names():    
    film_list = read_films(ratings_file)
    cPickle.dump(film_list, open('film_list.pickle', 'w+'))
    
def load_film_list():    
    return cPickle.load(open('film_list.pickle', 'r'))


def save_film_ratings():
    ratings_list = read_ratings(ratings_file)
    cPickle.dump(ratings_list, open('film_ratings_list.pickle', 'w+'))
    
def load_ratings_list():    
    return cPickle.load(open('film_ratings_list.pickle', 'r'))


def save_writer_films():
    writer_lines = get_writer_lines(writers_file)
    writer_films = pull_items(writer_lines)
    cPickle.dump(writer_films, open('writer_films.pickle', 'w+'))
    
def load_writer_films():    
    return cPickle.load(open('writer_films.pickle', 'r'))



    
def load_director_films():    
    return cPickle.load(open('director_films.pickle', 'r'))


"""first time running need to:

"""

save_film_names()
save_film_ratings()
save_writer_films()
save_director_films()

'''create list variables from file'''
film_list = load_film_list() if 'film_list' not in dir() else film_list
ratings_list = load_ratings_list() if 'ratings_list' not in dir() else ratings_list
writer_films = load_writer_films() if 'writer_films' not in dir() else writer_films
director_films = load_director_films() if 'director_films' not in dir() else director_films
