# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 14:12:49 2015

@author: emg
"""
###################################################################################
#TESTING ??? WITH TOP 250
###################################################################################

import itertools
from film_data_dump import director_films, writer_films
from film_data_dicts import make_reverse_dict, film_directors, film_writers
from pull_item_info import get_film_info, get_ratings, print_ratings


top_250_films = [line.split('  ')[-1].strip() for line in open('top_250.txt')]
top_250_ratings = [line.split('  ')[-2].strip() for line in open('top_250.txt')]

def get_top_250_directors():
    '''make list of directors of top 250 films'''
    results = []
    for film in top_250_films:
        if film in film_directors: #avoiding unicode issues  atm
            director = film_directors[film]
            results.append(director)
    results.sort() #make case-insensitive
    return results
    
top_250_directors = get_top_250_directors()

def get_top_250_writers():
    '''make list of writers of top 250 films'''
    results = []
    for film in top_250_films:
        if film in film_writers: #avoiding unicode issues  atm
            writer = film_writers[film]
            results.append(writer)
    results.sort() #make case-insensitive
    return results

top_250_writers = get_top_250_writers()

def get_top_250_film_info():
    result = []    
    for film in top_250_films:
        print film
        info = get_film_info(film)
        print info
        result.append(info)
    return result
    
top_250_info = get_top_250_film_info()

def rank_top_directors():
    '''make dict of (# of top 250 films) : director'''
    d = {}
    names = get_top_250_directors()
    for name in names:
        if str(name) in d:
            d[str(name)] += 1
        else:
            d[str(name)] = 1
    for name in d: # find better may to make ints str
        num = d[name]
        d[name] = str(num)
    result = make_reverse_dict(d)
    return result

def get_top_director_ratings(director):
    '''get ratings of all director's films in top 250'''
    ratings = []    
    films = director_films[director]
    for film in films:
        if film in top_250_films:
            rating = top_250_ratings[film]
            info = [film, rating]
            ratings.append(info)
    return ratings

def print_top_director_ratings(director):
    '''print film ratings for all director's films in top 250 + average'''
    ratings = get_top_director_ratings(director)
    s = 0
    print director
    print '-----------------------'
    for x in ratings:
        print '{}: {}'.format(x[1], x[0])
        s += float(x[1])
    avg = s / len(ratings)
    print '-----------------------'
    print avg, ': Average Rating'

def get_top_writer_ratings(writer):
    '''get ratings of all writer's films in top 250'''
    ratings = []    
    films = writer_films[writer] #is this the right format?
    for film in films:
        if film in top_250_films:
            rating = top_250_ratings[top_250_films.index(film)]
            info = [film, rating]
            ratings.append(info)
    return ratings

def print_top_writer_ratings(writer):
    '''print film ratings for all writer's films in top 250 + average'''    
    ratings = get_top_writer_ratings(writer)
    s = 0
    print writer
    print '-----------------------'
    for x in ratings:
        print '{}: {}'.format(x[1], x[0])
        s += float(x[1])
    avg = s / len(ratings)
    print '-----------------------'
    print avg, ': Average Rating'

######

ranked_directors = rank_top_250_directors()
'''make dict count of top 250 films : directors'''
counts_by_director = make_reverse_dict({k: [v] for k, v in ranked_directors.iteritems()})


#andy's version of best_directors
best_directors = list(itertools.chain(*[(i, counts_by_director[i]) for i in range(8, 0, -1)]))



#ella's version of best_directors
#def list_best_directors():
#    c = []
#    for k in counts_by_director:
#        info = [k]
#        for x in counts_by_director[k]:
#            info.append(x)
#        c.append(info)
#    c.sort(reverse=True)
#    for x in c:
#        for v in x:
#            print v
