import csv

CSVFILE = open('Data.gov_Catalog.csv')
# takes a list of column headers and creates a mapping
# of 'column name' -> 'index'
class ColumnMap(dict):

  def build_from(self, header_list):
    mapping = {}
    for index, name in enumerate(header):
      mapping[name] = index
    self[name] = mapping

def grab_header(csvfile_name):
  with open(csvfile_name) as csvfile:
    reader = csv.reader(csvfile)
    header = csv.next()
    map = ColumnMap()
    map.build_from(header)

    return map



empties = [map.keys()]
with open('Data.gov_Catalog.csv') as csvfile:
  reader = csv.DictReader(csvfile)

def run()
  with open(CSVFILE) as csvfile:

