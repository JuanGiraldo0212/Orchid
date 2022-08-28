import os
from uuid import UUID

from pymongo import MongoClient

user = os.environ.get('MONGODB_USR')
password = os.environ.get('MONGODB_PWD')
connection_string = 'mongodb://localhost:27017'
client = MongoClient(connection_string, uuidRepresentation='standard')
db = client.orchid


def insert_job(new_job):
    collection = db.jobs
    inserted_id = collection.insert_one(new_job).inserted_id
    return inserted_id


def retrieve_job(job_id):
    collection = db.jobs
    try:
        result = collection.find_one({'_id': UUID(job_id)})
    except ValueError:
        result = None
    return result


