# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 11:28:47 2015

@author: emg
"""

def make_directors_info_dict(film_info_d):
    d = {}
    for k, v in film_info_d.iteritems():
        if len(v[1]) == 1:
            name = v[1][0]
        else:
            for x in v[1]:
                name = x[1][0]
    info = (k, v[0], v[2])
    if name in set(d):
        d[name].append(info)
    else:
        d[name] = [info] 
    return d