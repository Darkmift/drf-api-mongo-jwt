#utils/mongo_utils.py
from pymongo import MongoClient
from decouple import config

def get_db_handle():
    db_uri = config('DB_URI')
    db_name = config('DB_NAME')

    client = MongoClient(db_uri)
    db_handle = client[db_name]
    return db_handle, client

def add_document(collection, data):
    db_handle, client = get_db_handle()
    result = db_handle[collection].insert_one(data)
    client.close()
    return result.inserted_id

def get_documents(collection, query):
    db_handle, client = get_db_handle()
    documents = list(db_handle[collection].find(query))
    client.close()
    return documents

def update_document(collection, query, new_values):
    db_handle, client = get_db_handle()
    result = db_handle[collection].update_one(query, {'$set': new_values})
    client.close()
    return result.modified_count

def delete_document(collection, query):
    db_handle, client = get_db_handle()
    result = db_handle[collection].delete_one(query)
    client.close()
    return result.deleted_count
