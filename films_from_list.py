# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 11:09:57 2015

@author: emg
"""

import pandas as pd
#panda.read_csv sep, skip rows, skip inital space?

# parser by andy
def read_ratings(filename, header=27):
    results = []
    for i, line in enumerate(open(filename)):
        if i > header:        
            result = line.split('  ')[-1].strip()
            results.append(result)

    return results

film_names = read_ratings('test.list')