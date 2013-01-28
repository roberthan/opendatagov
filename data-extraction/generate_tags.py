from lib.pymongo_connection import *
import re
from lib.stopwords import stopwords
from stemming.porter2 import stem
from sets import Set
matcher = re.compile("[^\w\-/']+")
stopdict = stopwords()
stem_dict = {}

db.catalog.remove()

def get_keywords(item):
    keywords = matcher.split(item['keywords'].replace('/','').replace('-','').strip().lower())
    keywords += (matcher.split(item['description'].replace('/','').replace('-','').strip().lower()))
    keywords += (matcher.split(item['name'].replace('/','').replace('-','').strip().lower()))
    return keywords
#get stems
for item in db.raw_catalog.find():
    kw = get_keywords(item)
    print kw
    for word in kw:
        #filter out numbers and more than 2 letters
        if not word.isdigit() and word.__len__() > 2:
            #stop words
            if not stopdict.has_key(word):
                #populate stems lookup table
                s = stem(word)
                if s.__len__() > 2:
#                    lk_up_result = db.stemmings.find_one({u'_id': s})
                    if not stem_dict.has_key(s) or stem_dict[s].__len__() > word.__len__():
                        stem_dict[s]=word
#                        db.stemmings.update({u'_id': s}, {"$set": {"r": word}},True)
#                    elif lk_up_result['r'].__len__() > word:
#                        db.stemmings.update({u'_id': s}, {"$set": {"r": word}},True)

#generate tags
for item in db.raw_catalog.find():
    i = {}
    i[u'_id'] = item['uid']
    i['u'] = item['url']
    i['a'] =item['agency']
    i['s']= item['source']
    i['n']= item['name']
    kw = get_keywords(item)
    print kw
    tags=[]
    for word in kw:
        s=stem(word)
        if stem_dict.has_key(s):
            tags.append(stem_dict[s])
    tags=list(Set(tags))
    print tags
    i['t']=tags
    db.catalog.insert(i)
#
#db.catalog.ensureIndex({ 't': 1 })
#db.catalog.ensureIndex({ 'n': 1 })
#db.catalog.ensureIndex({ 'a': 1 })