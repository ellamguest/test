# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 15:27:49 2015

@author: emg
"""

from read_film_files import read_films, ratings_file, read_ratings, get_writer_lines,\
writers_file, get_director_lines, directors_file
from line_processing import pull_items
from tools import make_reverse_dict


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

'''dict of film : director(s)'''
film_directors = make_reverse_dict(director_films)

'''dict of film : writer(s)'''
film_writers = make_reverse_dict(writer_films)

director_ratings_dict = {}

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