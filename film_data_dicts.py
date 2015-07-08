# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 15:27:49 2015

@author: emg
"""

from read_film_files import read_films, ratings_file, read_ratings, get_writer_lines,\
writers_file, get_director_lines, directors_file
from line_processing import pull_items


'''list of films A-Z'''
film_list = read_films(ratings_file)

'''dict of film : ratings'''
ratings_list = read_ratings(ratings_file)

'''list of raw lines from writers_file'''
writer_lines = get_writer_lines(writers_file)
'''dict of writer : filmography'''
writer_films = pull_items(writer_lines)

'''list of raw lines from directors_file'''
director_lines = get_director_lines(directors_file)
'''dict of director : filmography'''
director_films = pull_items(director_lines)

def make_reverse_dict(d):
    '''reverse any dict, accounting for possible multiple values'''
    results = {}
    for k, vs in d.iteritems():
        for v in vs:
            if v in results:
                results[v].append(k)
            else:
                results[v] = [k]
    return results

'''dict of film : director(s)'''
film_directors = make_reverse_dict(director_films)

'''dict of film : writer(s)'''
film_writers = make_reverse_dict(writer_films)