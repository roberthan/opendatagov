#generates placeholder data
from lib.pymongo_connection import *
from random import randrange
#test full-text search
for item in db.catalog.find( { 't' : "data" }, { 'n' : 1, 'u':1 } ):
    print item

