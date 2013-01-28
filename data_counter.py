__author__ = 'roberthan'
from pymongo_connection import *
from bson.son import SON
import json
def getWords(filter):
#    print filter
    if not filter == '':
        f = filter.split('-')
        pipe2 = [
            { '$match' : { 't' : { '$all': f }} },
            {"$unwind": "$t"},
            { '$group' : {
                '_id' : "$t"
                , "count": {"$sum": 1}
            } },
            {"$sort": SON([("count", -1), ("_id", -1)])},
            { "$limit" : 50 }
            ]
    else:
        pipe2 = [
            {"$unwind": "$t"},
            { '$group' : {
                '_id' : "$t"
                , "count": {"$sum": 1}
            } },
            {"$sort": SON([("count", -1), ("_id", -1)])},
            { "$limit" : 50 }
        ]
    eps = db.catalog.aggregate(pipeline=pipe2)
    eps = json.dumps(eps['result'])
    print eps
    return eps
if __name__ == '__main__':
    getWords('data-toxic')
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
