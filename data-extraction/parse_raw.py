#read each row in the csv and insert raw data into raw_catalog_records collection
from lib.pymongo_connection import *
import csv

with open('catalog.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        item = {}
        item['keywords'] = row['Keywords']
        item['description'] = row['Description']
        item['raw_name'] = row['Name']
        item['agency'] = row['Agency']
        item['uid'] = row['Uid']
        item['source'] = 'data.gov'
        item['url'] = 'https://datagov.socrata.com/'+row['Name'].rsplit('(').pop().replace(')','')
        item['name'] = row['Name'].split('(')[0]
        db.raw_catalog.insert(item)
