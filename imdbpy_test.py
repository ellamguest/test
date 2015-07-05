# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 11:40:33 2015

@author: emg
"""

from imdb import IMDb

ia = IMDb()

media = 'Hannibal'

search_result = ia.search_movie(media)

#choose first result from search
project = search_result[0]
ia.update(project)

director = project['director']
directors = list()
for item in director:
    directors.append(str(item))

#figure out how to print ech item of a list of any length
#print '{} is directed by {}'.format(project, directors)

writers = project['writer']
head_writer = writers[0]

print 'The head writer of {} is {}'.format(project, head_writer)


runtime = project['runtime']
runtime = runtime[0]
runtime = runtime.encode('utf8')


#print 'The {} runtime is {} mins'.format(media, runtime)

rating = project['rating']

#print '{} is rate {} on IMDB'.format(media, rating)

