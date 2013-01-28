import csv
from lib.pymongo_connection import *

lkup_cat = {}
with open('lkup_category.csv','rU') as category_lkup:
    reader = csv.DictReader(category_lkup)
    for row in reader:
        lkup_cat[row['Agency']] =row['Category']
print lkup_cat

for item in db.catalog.find():
    if item['a']:
        if lkup_cat.has_key(item['a']):
            print lkup_cat[item['a'].replace('.','')]
            db.catalog.update({u'_id': item['_id']}, {"$set": {"c": lkup_cat[item['a']]}})