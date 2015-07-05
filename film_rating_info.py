# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 10:23:38 2015

@author: emg
"""

import pandas as pd
from imdb import IMDb

ia = IMDb()

# list of 10 highest grossing films of all time
#film_names = ['Avatar', 'Titanic', 'The Avengers', 'Furious 7', 'Avengers: Age of Ultron', 'Harry Potter and the Deathly Hallows: Part 2', 'Jurassic World', 'Frozen', 'Iron Man 3', 'Transformers: Dark of the Moon']

def read_ratings(filename, header=27):
    results = []
    for i, line in enumerate(open(filename)):
        if i > header:        
            result = line.split('  ')[-1].strip()
            results.append(result)

    return results

film_names = read_ratings('test.list')



# list of film objects
film_objects = []
for x in film_names:
    search_result = ia.search_movie(x)
    project = search_result[0]
    ia.update(project)
    film_objects.append(project)


# dict of film objects : director, HEAD writer, rating
film_info = {}
for x in film_objects:
    director = x['director']
    writers = x['writer']
    head_writer = writers[0]
    rating = x['rating']
    info = (director, head_writer, rating)
    film_info[x] = info


# list of all directors obejcts
all_directors = []
for x in film_objects:
    all_directors.append(x['director'][0])
# list of all directors names
all_director_names = []
for x in all_directors:
    all_director_names.append(x['name'])


# list of all HEAD writers
all_writers = []
for x in film_objects:
    all_writers.append(x['writer'][0])
# list of all HEAD writers names
all_writer_names = []
for x in all_writers:
    all_writer_names.append(x['name'])


# list of all ratings
all_ratings = []
for x in film_objects:
    all_ratings.append(x['rating'])


#make series of names
film_series = pd.Series(film_names)
print film_series
director_series = pd.Series(all_director_names)
writer_series = pd.Series(all_writer_names)
rating_series = pd.Series(all_ratings)

series_dict = {'film' : film_series, 'director' : director_series, 'writer' : writer_series, 'rating' : rating_series}


df = pd.DataFrame(columns = ['film', 'director', 'writer', 'rating'], data = zip(film_series, director_series, writer_series, rating_series))

print df