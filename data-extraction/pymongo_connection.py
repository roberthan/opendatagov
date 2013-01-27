from pymongo import Connection

connection = Connection('54.235.168.23', 27017)
db = connection.opendatagov
#db.auth("mongoadmin", "anadminpassword")
raw_catalog = db.raw_catalog
samples = db.samples
