__author__ = 'roberthan'
#generates placeholder data
from lib.pymongo_connection import *
from random import randrange
#example_item['type']='Tabular'
#example_item['name']='White House Visitor Records  (dataset/White-House-Visitor-Records-Requests/644b-gaut)'
#example_item['keywords']='visitor records, white house, transparency, government'
#example_item['category']='0'
#example_item['description']='A list of White House Visitor Record requests.'
test_string = 'The Residential Energy Consumption Survey (RECS), which is conducted every four years, provides national statistical survey data on the use of energy in residential housing units including physical housing unit types, appliances utilized, demographics, fuels, and other energy use information. This dataset (i.e., the full RECS dataset) is very large in size and may require specialized software to open on your computer. The file might not open completely in Excel 2003 or earlier versions. For a subset of the data pertaining only to Energy Consumption component of RECS, please go to: http://www.data.gov/details/59'
for letter in test_string.split():
    example_item = {}
    example_item['w']=letter.upper()
    example_item['c']=randrange(500)
    example_item['f']='test'
    example_item['u']='http://google.com'
    samples.insert(example_item)
