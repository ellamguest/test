# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 12:14:04 2015

@author: andy
"""
import pdb
import re

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

pattern = '.*\((?:\d|\?){4}(?:\/[IVX]+)?\)'

def read_writer_films(filename, header=301):
    regex = re.compile(pattern)    
    
    results = []
    n = -1
    for i, line in enumerate(open(filename)):
#        if i % 100 == 0:
#            print 'processing line {}'.format(i)
        if i > header:  
            line = line.strip() 
            line = line.split('\t')
            line = filter(None, line) #is this still needed?
            if line != []: #better way to skip empty lines?
            # if the first item doesn't contain a year it's a name            
                if re.search(pattern, line[0]) == None:
                    n += 1                
                    name = line[0]
                    item = line[1]
                    item = regex.findall(item)[0]
                    results.append([item])
                # year is found, first term not name
                if re.search(pattern, line[0]) != None:
                    item = line[0] #why 1 out of range?
                    item = regex.findall(item)[0]
                    results[n].append(item)
    return results



data = [''''Abd Al-Hamid, Ja'far	Just Outside the Frame: The Profilmic Event and Beyond (2008)  (writer)''', '''
			Mesocaf\E9 (2011)  (written by)''',
'           '
 ''''Dada' Pecori, Diego	Adam (????)''', '''
			Cantarella (2011)  (story)''',
 '''A. Nolan, Simon		Two Worlds (2015/II)  (writer)''',
 '''A, Salman		The Ride (2015/II)  (writer)''']

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

def pull_items2(data):
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



#############################################################
#NO USE MAPPING TO PREVIOUS BC SOME HAVE MULTIPLE ENTRIES
############################################################
#####old attempt, not gonna work for multiples
def pull_items(lines):
    for line in lines:
        line = format_line(line)
        if line == []: #better way to skip empty lines?
            lines.remove(line)
    n = -1
    regex = re.compile(pattern)     
    results = []
    while n < len(lines):
        previous = lines[n]
        current = lines[n+1]    
        print n, 'previous', previous
        print n, 'current', current
            # if the first item doesn't contain a year it's a name            
        if re.search(pattern, line[0]) == None:
            name = line[0]                        
            item = line[1]
            item = regex.findall(item)[0]
            print 'name', name
            print 'item', item
            results.append([name, item])
    #            results[name] = [item]
    #            print results
            # year is found, first term not name
    ## HOW TO MAP ITEM TO NAME FROM PREVIOUS LINE  
        if re.search(pattern, line[0]) != None:
            item = line[0] #why 1 out of range?
            print 'name', name
            print 'item', item
    #            print 'item', item
            item = next(regex.finditer(item)).string
            return item
    #            values = results[name]
    #            values.append(item)
    #            results[name] = values            
    #            print results
        n += 1
    return results

def writer_filmographies(writer_names, writer_films):
    if len(writer_names) != len(writer_films):
        print 'Writer names and films don\'t match!'
    d = {}
    n = 0
    while n < len(writer_names):
        d[writer_names[n]] = writer_films[n]
        n += 1
    return d

def get_director_lines(filename, header=234):
    results = []
    for i, line in enumerate(open(filename)):
        if i > header:        
            results.append(line)

    return results

director_lines = get_director_lines('directors_test.list')

director_films = pull_items2(director_lines)

for x in director_films:
    print 'name', x
    print 'films', director_films[x] 

