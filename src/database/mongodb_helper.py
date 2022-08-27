import os
from pymongo import MongoClient

password = os.environ.get("MONGODB_PWD")
connection_string = ""
client = MongoClient(connection_string)


