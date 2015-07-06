# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 12:14:04 2015

@author: andy
"""
import pdb
import re

writers_file = 'writers.list'
directors_file = 'directors.list'
ratings_file = 'test.list'

def read_films(filename, header=27):
    results = []
    for i, line in enumerate(open(filename)):
        if i > header:        
            result = line.split('  ')[-1].strip()
            results.append(result)

    return results

def read_ratings(filename, header=27):
    results = {}
    for i, line in enumerate(open(filename)):
        if i > header:        
            name = line.split('  ')[-1].strip()
            rating = line.split('  ')[-2].strip()
            results[name] = [rating]

    return results

def get_writer_lines(filename, header=301):
    results = []
    for i, line in enumerate(open(filename)):
        if i > header:        
           results.append(line)
    return results

def get_director_lines(filename, header=234):
    results = []
    for i, line in enumerate(open(filename)):
        if i > header:        
            results.append(line)
    return results

film_names = read_films(ratings_file)
film_ratings = read_ratings(ratings_file)
writer_lines = get_writer_lines(writers_file)
director_lines = get_director_lines(directors_file)


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

pattern = '.*\((?:\d|\?){4}(?:\/[IVXL]+)?\)'

def pull_items(data):
    lines = format_lines(data)
    regex = re.compile(pattern)
    results = {}
    n = 0
    while n < len(lines):
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

writer_films = pull_items(writer_lines)
director_films = pull_items(director_lines)

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
    
d = make_film_dict(film_names)

print d
        

