from pymongo_connection import *

for item in db.key_terms.find():
    i = {}
    if item['value'].has_key('key'):
        i['_id'] = item['value']['key']
        print item['_id']
#    else:
#        print item['_id']
#    print item['value']['count']