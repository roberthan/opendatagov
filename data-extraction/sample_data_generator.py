__author__ = 'roberthan'
#generates placeholder data
from pymongo_connection import *
example_item = {}
example_item['uid']='0'
example_item['type']='Tabular'
example_item['name']='White House Visitor Records  (dataset/White-House-Visitor-Records-Requests/644b-gaut)'
example_item['keywords']='visitor records, white house, transparency, government'
example_item['category']='0'
example_item['description']='A list of White House Visitor Record requests.'
samples.insert(example_item)
