# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 15:30:53 2015

@author: emg
"""

import re

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

'''year marker to differentiate names from films'''
pattern = '.*\((?:\d|\?){4}(?:\/[IVXL]+)?\)'

def pull_items(data):
    print 'Formatting lines...'
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
            if item not in results[name]: #preventing duplicates
                results[name].append(item)
        else:
            results[name] = [item]
        if n%100000 == 0:
            print n, line
    return results