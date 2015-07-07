# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 12:14:04 2015

@author: emg
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
        line = lines[n]
#        print n, line
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
#PULL, FORMAT, AND DUMP INFO
###################################################################################

def save_film_names():    
    film_names = read_films(ratings_file)
    cPickle.dump(film_names, open('film_list.pickle', 'w+'))
    
def load_film_list():    
    return cPickle.load(open('film_list.pickle', 'r'))

#save_film_names()
#film_list = load_film_list() if 'film_list' not in dir() else film_list

def save_film_ratings():
    film_ratings = read_ratings(ratings_file)
    print 'Dumping now'
    cPickle.dump(film_ratings, open('film_ratings_list.pickle', 'w+'))

def load_ratings_list():    
    return cPickle.load(open('film_ratings_list.pickle', 'r'))

#save_film_ratings()
#ratings_list = load_ratings_list() if 'ratings_list' not in dir() else ratings_list

def save_writer_films():
    writer_lines = get_writer_lines(writers_file)
    writer_films = pull_items(writer_lines)
    cPickle.dump(writer_films, open('writer_films.pickle', 'w+'))
    
def load_writer_films():    
    return cPickle.load(open('writer_films.pickle', 'r'))

#pdb.set_trace()

writer_films = load_writer_films() if 'writer_films' not in dir() else writer_films

def save_director_films():
    director_lines = get_director_lines(directors_file)
    director_films = pull_items(director_lines)
    cPickle.dump(director_films, open('director_films.pickle', 'w+'))
    
def load_director_films():    
    return cPickle.load(open('director_films.pickle', 'r'))

#pdb.set_trace()

director_films = load_director_films() if 'director_films' not in dir() else director_films

"""first time running need to:
save_film_names()
save_film_ratings()
save_writer_films()
save_director_films()
"""

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
    rating = ratings_list[film]
    director = search_filmographies(film, director_films)
    writer = search_filmographies(film, writer_films)
    info = [rating, director, writer]
    return info

def print_film_info(film):
    info = get_film_info(film)
    print 'Film: {}'.format(film)
    print 'Rating: {}'.format(info[0])
    print 'Director(s): {}'.format(info[0])
    print 'Writers(s): {}'.format(info[0])

def get_director_ratings(director):
    ratings = []    
    films = director_films[director] #is this the right format?
    for film in films:
        rating = ratings_list[film]
        info = [film, rating]
        ratings.append(info)
    return ratings

################################################################################
## IF I WANT A FULL COPY OF FILM : INFO?!?!
################################################################################
#def make_film_dict(film_list):
#    d = {}
#    for film in film_list:
#        info = get_film_info(film)
#        if info[1] != [] and info[2] != []:
#            print film, info
#            d[film] = info
#    return d

#def save_film_dict():
#    film_dict = make_film_dict(film_list)
#    cPickle.dump(film_dict, open('film_dict.pickle', 'w+'))
#    
#def load_film_dict():    
#    return cPickle.load(open('film_dict.pickle', 'r'))


#save_film_dict()
#film_dict = load_film_dict if 'film_dict' not in dir() else film_dict

#d = make_film_dict(film_names) ----------- test last
#
#for x in d:
#    print x
#    print d[x]
#    print ''

###############################################################################
#MAKE REVERSE DICTS
###############################################################################
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


###################################################################################
#TEST WITH TOP 250
###################################################################################

#pdb.set_trace()

top_250_films = [line.split('  ')[-1].strip() for line in open('top_250.txt')]

#pdb.set_trace()

top_250_ratings = [line.split('  ')[-2].strip() for line in open('top_250.txt')]
    

def get_top_directors():
    for film in films:
    ...

def get_top_director_ratings(director):
    ratings = []    
    films = director_films[director] #is this the right format?
    for film in films:
        if film in top_250_films:
            rating = top_250_ratings[top_250_films.index(film)]
            info = [film, rating]
            ratings.append(info)
    return ratings

def print_top_director_ratings(director):
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
    ratings = []    
    films = writer_films[writer] #is this the right format?
    for film in films:
        if film in top_250_films:
            rating = top_250_ratings[top_250_films.index(film)]
            info = [film, rating]
            ratings.append(info)
    return ratings

def print_top_writer_ratings(writer):
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

#print_top_director_ratings('Spielberg, Steven')

def get_top_250_directors()
    results = []
    for film in top_250_films:
        if film in film_directors: #avoiding unicode issues atm
            director = film_directors[film]
            results.append(director)
    results.sort() #make case-insensitive
    return results

def rank_top_250_directors():
    d = {}
    names = get_top_250_directors()
    for name in names:
        if str(name) in d:
            d[str(name)] += 1
        else:
            d[str(name)] = 1
    result = make_reverse_dict(d)
    return d
    
def get_250_writers():
    pass

counts_by_director = make_reverse_dict({k: [v] for k, v in ranked_directors.iteritems()})

best_directors = list(itertools.chain(*[(i, counts_by_director[i]) for i in range(8, 0, -1)])) #andy's code

#def list_best_directors(): ella's version of best_directors
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