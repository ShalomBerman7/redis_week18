from pymongo import MongoClient
from os import getenv

uri = getenv('MONGO_URI', 'mongodb://localhost:27017/')
mongo_db = getenv("MONGO_DB", "week18_redis")
mongo_collection = getenv("MONGO_COLLECTION", "week18")

client = MongoClient(uri)
db = client[mongo_db]
collection = db[mongo_collection]
