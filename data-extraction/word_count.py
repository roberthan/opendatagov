from lib.pymongo_connection import *
from bson.code import Code
db.test_results.remove()
import datetime

mapper = Code("""
               function () {
                 this.t.forEach(function(z) {
                    var value = {
                        count: 1,
                        u: z
                    };
                    emit(z, value);
                 });
               }
               """)

reducer = Code("""
                function (key, values) {
                  var obj = {
                    url:[],
                    count:0;
                  };
                  values.forEach( function(value) {
                    obj.url[obj.count] = value.u;
                    obj.count += value.count;
                    }
                  )
                  return obj;
                }
                """)

result = db.catalog.map_reduce(mapper, reducer, "test_results", query={ 't' : "open" })
for doc in result.find():
   print doc

