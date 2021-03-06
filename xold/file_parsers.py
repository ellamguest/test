# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 12:14:04 2015

@author: emg
"""

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






