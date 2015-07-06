# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 12:14:04 2015

@author: andy
"""
import pdb
import re
import cPickle

writers_file = 'writers.list'
directors_file = 'directors.list'
ratings_file = 'ratings.list'

pattern = '.*\((?:\d|\?){4}(?:\/[IVXL]+)?\)' #year marker to differentiate names from films

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

def get_writer_lines(filename, header=301, footer=3582903):
    results = []
    for i, line in enumerate(open(filename)):
        if header < i <= footer:        
            print i, 'writer', line
            results.append(line)
    return results

def get_director_lines(filename, header=234, footer=2244913):
    results = []
    for i, line in enumerate(open(filename)):
        if header < i <= footer:
            print i, 'director', line
            results.append(line)
    return results

###################################################################################
#CREATE LINES VARAIBLES
###################################################################################

#film_names = read_films(ratings_file)
#film_ratings = read_ratings(ratings_file)
#writer_lines = get_writer_lines(writers_file)
director_lines = get_director_lines(directors_file)

###################################################################################
#BREAK LINES INTO ITEMS
###################################################################################
def format_line(line):    
    line = line.strip()
    line = line.split('\t')
    line = filter(None, line) #is this still needed?
    return line

def format_lines(lines):
    new_lines = []    
    for line in lines:
        new = format_line(line)
        if new == []: #better way to skip empty lines?
            pass
        else:
            new_lines.append(new)
    return new_lines

def pull_items(data):
    lines = format_lines(data)
    regex = re.compile(pattern)
    results = {}
    n = 0
    while n < len(lines):
        print n
        line = lines[n]
        if re.search(pattern, line[0]) == None:
            name = line[0]
            item = line[1]
        else:
            item = line[0]
        item = regex.findall(item)[0]
        n += 1
        if name in results:
            results[name].append(item)
        else:
            results[name] = [item]
    return results
 

###################################################################################
#DUMP INFO
###################################################################################
def save_film_names():
    cPickle.dump(film_names, open('film_list.pickle', 'w+'))
    
def load_film_list():    
    return cPickle.load(open('film_list.pickle', 'r'))

#film_list = load_film_list() if 'film_list' not in dir() else film_list ------------ test these 1 at a time

def save_film_ratings():
    cPickle.dump(film_ratings, open('film_ratings_list.pickle', 'w+'))

def load_ratings_list():    
    return cPickle.load(open('film_ratings_list.pickle', 'r'))

#ratings_list = load_ratings_list() if 'ratings_list' not in dir() else ratings_list

def save_writer_films():
    writer_films = pull_items(writer_lines)
    cPickle.dump(writer_films, open('writer_films.pickle', 'w+'))
    
def load_writer_films():    
    return cPickle.load(open('writer_films.pickle', 'r'))

#writer_films = load_writer_films() if 'writer_films' not in dir() else writer_films

def save_director_films():
    director_films = pull_items(director_lines)
    cPickle.dump(director_films, open('director_films.pickle', 'w+'))
    
def load_director_films():    
    return cPickle.load(open('director_films.pickle', 'r'))

#director_films = load_director_films() if 'director_films' not in dir() else director_films

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
    rating = film_ratings[film]
    director = search_filmographies(film, director_films)
    writer = search_filmographies(film, writer_films)
    info = [rating, director, writer]
    return info

def make_film_dict(film_names):
    d = {}
    for film in film_names:
        info = get_film_info(film)
        d[film] = info
    return d

#d = make_film_dict(film_names) ----------- test last
#
#for x in d:
#    print x
#    print d[x]
#    print ''

###################################################################################
#DUMP FILMOGRAPHY DICT
###################################################################################
        
def save_film_dict():
    film_dict = make_film_dict(film_names)
    cPickle.dump(film_dict, open('film_dict.pickle', 'w+'))
    
def load_film_dict():    
    return cPickle.load(open('film_dict.pickle', 'r'))

#film_dict = load_film_dict if 'film_dict' not in dir() else film_dict
