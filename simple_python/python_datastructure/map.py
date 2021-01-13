"""Python Maps also called ChainMap is a type of data structure to 
manage multiple dictionaries together as one unit. The combined 
dictionary contains the key and value pairs in a specific sequence 
eliminating any duplicate keys. The best use of ChainMap is to search 
through multiple dictionaries at a time and get the proper key-value pair mapping."""
from __future__ import absolute_import
import collections


dict1 = {'day1': 'Mon', 'day2': 'Tue'}
dict2 = {'day3': 'Wed', 'day1': 'Thu','day2': 'Tue'}

res = collections.ChainMap(dict2, dict1)

# creating single dictionary
print(res.maps,'\n')
print(list(res.keys()))
print(list(res.values()))