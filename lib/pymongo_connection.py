from pymongo import Connection

connection = Connection('data2.me', 27017)
db = connection.opendatagov
#db.auth("mongoadmin", "anadminpassword")
raw_catalog = db.raw_catalog
samples = db.samples
