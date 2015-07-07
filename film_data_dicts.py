# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 15:27:49 2015

@author: emg
"""

from film_data_dump import director_films, writer_films

def make_reverse_dict(d):
    results = {}
    for k, vs in d.iteritems():
        for v in vs:
            if v in results:
                results[v].append(k)
            else:
                results[v] = [k]
    return results

film_directors = make_reverse_dict(director_films)

film_writers = make_reverse_dict(writer_films)

