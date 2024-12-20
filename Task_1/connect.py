from pymongo import MongoClient

uri = "mongodb://172.22.0.1:27017/"

client = MongoClient(uri)

#db = client.tes
try:
    dbs = client.mydatabase.command("ping")
    print("Connected to MongoDB successfully!")
    
    client.close()
except Exception as e:
    raise Exception(
        "The following error occured,", e
    )
