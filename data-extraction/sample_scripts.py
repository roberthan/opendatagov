#generates placeholder data
from lib.pymongo_connection import *
from random import randrange
from bson.code import Code

#test full-text search
for item in db.catalog.find( { 't' : "data" }, { 'n' : 1, 'u':1 } ):
    print item

mapper = Code("""
               function () {
                 this.t.forEach(function(z) {
                   emit(z, 1);
                 });
               }
               """)

reducer = Code("""
                function (key, values) {
                  var total = 0;
                  for (var i = 0; i < values.length; i++) {
                    total += values[i];
                  }
                  return total;
                }
                """)

result = db.catalog.map_reduce(mapper, reducer, "test_results", query={ 't' : "open" })
for doc in result.find():
    print doc
