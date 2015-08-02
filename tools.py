# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 13:20:59 2015

@author: emg
"""

def check_in_dict(name, d):
    “””name should be in last, first format”””
    name = name.title()
    return [n for n in d if name in n]

def make_reverse_dict(d):
    '''reverse any dict, accounting for possible multiple values'''
    results = {}
    for k, vs in d.iteritems():
        for v in vs:
            if v in results:
                results[v].append(k)
                results[v] = list(set(results[v]))
            else:
                results[v] = [k]
    return results
    
def frequency_dict(names):
    '''make dict of # : names'''
    d = {}
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

def most_popular(names):
    d = frequency_dict(names)
    p = []
    for k, v in d.iteritems():
        n = [k]
        for x in v:
            n.append(x)
        p.append(n)
    p.sort(reverse=True)
    return p

