# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 12:14:04 2015

@author: emg
"""

writers_file = 'writers.list'
directors_file = 'directors.list'
ratings_file = 'ratings.list'

#make arrays from not lists? stacks of queues?

def read_films(filename, header=281407, footer=633534):
    '''creates list of film names from ratings_file'''
    results = []
    for i, line in enumerate(open(filename)):
        if header < i <= footer:          
            result = line.split('  ')[-1].strip()
            results.append(result)
            if i%1000 == 0:
                print i, 'film', result
    return results

def read_ratings(filename, header=281407, footer=633534):
    '''creates dict of film names : rating from ratings_file'''
    results = {}
    for i, line in enumerate(open(filename)):
        if header < i <= footer:       
            name = line.split('  ')[-1].strip()
            rating = line.split('  ')[-2].strip()
            results[name] = rating
            if i%1000 == 0:
                print i, 'rating', rating, name
    return results
    
#previous footer=3582903

def get_writer_lines(filename, header=301, footer=4101660):
    '''creates list of lines from writers_file'''
    results = []
    for i, line in enumerate(open(filename)):
        if header < i <= footer:        
            results.append(line)
            if i%1000 == 0:
                print i, 'writer', line
    return results

#previous footer=2244913

def get_director_lines(filename, header=234, footer=2639293):
    '''creates list of lines from directors_file'''
    results = []
    for i, line in enumerate(open(filename)):
        if header < i <= footer:
            results.append(line)
            if i%1000 == 0:
                print i, 'director', line
    return results




