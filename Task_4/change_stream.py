from pymongo import MongoClient
from pymongo.errors import PyMongoError

client = MongoClient("mongodb://172.22.0.1:27017/?replicaSet=rs0")
db = client["ecommerce"]  
orders_collection = db["orders"]

try:
    with orders_collection.watch() as change_stream:
        print("Watching changes in the 'orders' collection...")
        for change in change_stream:
            print("Change detected:")
            print(change)
except PyMongoError as e:
    print(f"Error watching changes: {e}")
