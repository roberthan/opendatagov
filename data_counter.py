__author__ = 'roberthan'
from pymongo_connection import *
from bson.son import SON
import json
RESULTS = 100

def getWords(filter):
    if not filter == '':
        f = filter.split('-')
        pipe2 = [
            { '$match' : { 't' : { '$all': f }} },
            {"$unwind": "$t"},
            { '$group' : {
                '_id' : "$t"
                , "count": {"$sum": 1}
                ,'category': { "$addToSet": "$c"}
            } },
            {"$sort": SON([("count", -1), ("_id", -1)])},
            { "$limit" : RESULTS }
            ]
    else:
        pipe2 = [
            {"$unwind": "$t"},
            { '$group' : {
                '_id' : "$t"
                , "count": {"$sum": 1}
                ,'category': { "$addToSet": "$c"}
            } },
            {"$sort": SON([("count", -1), ("_id", -1)])},
            { "$limit" : RESULTS }
        ]
    eps = db.catalog.aggregate(pipeline=pipe2)
    eps = json.dumps(eps['result'])
#    print eps
    return eps
def getDetails(filter):
    if not filter == '':
        f = filter.split('-')
        query = db.catalog.find( { 't' : { '$all': f } }, { 'n' : 1, 'u':1, 'c':1 } )
    else:
        query = db.catalog.find()
        #        eps = json.dumps(db.catalog.find( { 't' : { '$all': f } }, { 'n' : 1, 'u':1 } ).limit(50)['result'])
#        print eps
    meta = {}
    meta['count'] = query.count()
    i = 0
    arr=[]
    for item in query.limit(50):
        i = {}
#        print item['n']
#        print item['u']
        i['name']=item['n']
        i['url']=item['u']
        if item.has_key('c'):
            i['category']=item['c']
        else:
            i['category']=''
        arr.append(i)
    eps = {}
    eps['meta']=meta
    eps['results']=arr
#    print eps
    return json.dumps(eps)

if __name__ == '__main__':
    getDetails('toxic')
#    getDetails('')
#    getWords('data-toxic')
#        arr = samples.find({"f": filter})
#    else:
#        arr = samples.find()
#    print db.catalog.aggregate([
#            {"$unwind": "$t"},
#            {"$group": {"_id": "$t", "count": {"$sum": 1}}},
#            {"$sort": SON([("count", -1)])}
#        ])
#    pipe = [
##        {'$match':{'category':'In'}},
#        { '$group' : {
#            '_id' : "$value"
#        } }
#    ]

#    eps = db.key_terms.aggregate(pipeline=pipe)

#    choices = []
#    count = 0
#    for term in str_value.lower().replace('-',' ').split(' '):
#        count +=1
#        if count>=4:
#            break;
#        #        choices += search_db.find({"kw": term})
#        for item in
#        #            print item['name']
#            if not item['name'] in choices:
#                choices = choices + [item['name']]
#            #            choices = f7(choices)
#            #    print TEST_STR
#    choices = f7(choices)
#    results = dict(process.extract(str_value, f7(choices), limit=3))
#    res = list(sorted(results, key=results.__getitem__, reverse=True))
#    print res
#    if res:
#        if results[res[0]] >= 95:
#            return [res[0]]
#        #        elif results[res[0]] +results[res[1]]+results[res[2]] >= 245:
#        #            return res[:3]
#        else:
#            return res
#    else:
#        return []
