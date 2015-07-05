# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 12:14:04 2015

@author: andy
"""

def read_films(filename, header=27):
    results = []
    for i, line in enumerate(open(filename)):
        if i > header:        
            result = line.split('  ')[-1].strip()
            results.append(result)

    return results

film_names = read_films('test.list')

def read_ratings(filename, header=27):
    results = {}
    for i, line in enumerate(open(filename)):
        if i > header:        
            name = line.split('  ')[-1].strip()
            rating = line.split('  ')[-2].strip()
            results[name] = [rating]

    return results

film_ratings = read_ratings('test.list')


def read_writers(filename, header=301):
    results = []
    for i, line in enumerate(open(filename)):
        if i > header:        
            result = line.split('	')[0].strip()
            if result != '':
                results.append(result)

    return results

writer_names = read_writers('writers_test.list')

def read_writer_films(filename, header=301):
    results = []
    n = -1
    for i, line in enumerate(open(filename)):
        if i > header:        
            name = line.split('	')[0].strip()
            if name == '':
                item = line.split('	')
                item = filter(None, item)
                item = item[0].strip()
                results[n].append(item)
            if name != '':
                item = line.split('	')
                item = filter(None, item)
                item = item[1].strip()
                results.append([item])
    return results

writer_films = read_writer_films('writers_test.list')

def writer_filmographies(writer_names, writer_films):
    if len(writer_names) != len(writer_films):
        print 'Writer names and films don\'t match!'
    d = {}
    n = 0
    while n < len(writer_names):
        d[writer_names[n]] = writer_films[n]
        n += 1
    return d
        

writer_filmographies = writer_filmographies(writer_names, writer_films)

for x in writer_filmographies:
    print x
    print writer_filmographies[x]\

    

def read_directors(filename, header=233):
    results = []
    for i, line in enumerate(open(filename)):
        if i > header:        
            result = line.split('	')[0].strip()
            if result != '':
                results.append(result)

    return results

director_names = read_directors('directors.list')


