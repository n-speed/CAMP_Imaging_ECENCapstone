import os
import json
from pymongo import MongoClient
import time

# MongoDB connection information
mongo_host = "mongodb+srv://sethroyder:l427r7bjOEpyBuKf@capstonecluster.d4azdqr.mongodb.net/"  # Change to your MongoDB server hostname or IP address
mongo_port = 27017  # Change to your MongoDB server port
db_name = "test"
collection_name = "collection_test"

# Connect to MongoDB
client = MongoClient(mongo_host, mongo_port)
db = client[db_name]
collection = db[collection_name]

# Retrieve all documents from the collection
all_documents = collection.find()

# Print or process the retrieved documents
#for document in all_documents:
#   print(document)

print(all_documents[0]["_id"])


client.close()
