import pymongo

# TODO - Replace DATABASE-URL with your mongodb database url
db_connection = pymongo.MongoClient("DATABASE-URL")
database = db_connection["pmanager"]
data = database["passwords"]
admin = database["admin"]
