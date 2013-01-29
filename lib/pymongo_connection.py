from pymongo import Connection
import os

if "DATA2ME_PROD" in os.environ:
    connection = Connection('0.0.0.0', 27017)
else:
    connection = Connection('data2.me', 27017)
db = connection.opendatagov
raw_catalog = db.raw_catalog
