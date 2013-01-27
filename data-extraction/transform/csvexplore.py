import csv
import re
from collections import Counter
from stemming.porter2 import stem
from stopwords import stopwords
#CSVFILE = open('Data.gov_Catalog.csv')

# takes a list of column headers and creates a mapping
# of 'column name' -> 'index'
class ColumnMap(dict):

  def build_from(self, header_list):
    mapping = {}
    for index, name in enumerate(header):
      mapping[name] = index
    self[name] = mapping

def build_map(csvfile_name):
  reader = csv.reader(csvfile)
  header = csv.next()
  map = ColumnMap()
  map.build_from(header)

  return map


stopdict = stopwords()
matcher = re.compile("[^\w\-/']+")
#matcher = re.compile("[\W^\-^']+")
keywords_all = []
with open('../datasource/Data.gov_Catalog.csv') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    keywords = row['Keywords']
    keyword_list = matcher.split(keywords)
    stripped_list = map(lambda x: x.strip(), keyword_list)
    filtered_list = []
    for word in stripped_list:
      if not stopdict.has_key(word):
        if word.upper() == word:
          filtered_list.append(word)
        else:
          filtered_list.append(word.lower())
    #stemmed_list = map(lambda x: stem(x), filtered_list)
    keywords_all += filtered_list

#print keywords_all
print Counter(keywords_all)

