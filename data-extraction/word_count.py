from lib.pymongo_connection import *
from bson.code import Code
db.key_terms.remove()
import datetime

mapper = Code("""
               function () {
                var self = this;
                 this.t.forEach(function(z,index,item) {
                    var value = {
                        count: 1
                        , url:{}
                        , agency:"data.gov"
                    };
                    value.url[self.n] = self.u;
                    var temp = '';
                    if(typeof self.c !== 'undefined'){
                        temp=self.c+'-';
                        value['category']=self.c;
                    }
                    else{
                        value['category']='';
                    }
                    value['key']=z;
                    emit(temp+z, value);
                 });
               }
               """)

reducer = Code("""
                function (key, values) {
                var obj = {
                    url:{},
                    count:0,
                    agency:"data.gov"
                  };
                var key_values = key.split('-')
                    if(key_values.length>1){
                        obj['key']=key_values[1];
                        obj['category']=key_values[0];
                    }
                    else{
                        obj['key']=key_values[0];
                    }
                  for (var i = 0; i < values.length; i++) {
                    obj.count += values[i].count;
                    obj.url[values[i].name]=values[i].url
                  }
                  return obj;
                }
                """)
#, query={ 't' : "open" }
result = db.catalog.map_reduce(mapper, reducer, "key_terms")
#result = db.catalog.map_reduce(mapper, reducer, "test_results", query={ 't' : { '$all': [ "toxic", "data" ] }})
for doc in result.find():
   print doc

