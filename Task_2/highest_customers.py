from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://172.22.0.1:27017")
db = client["ecommerce"]

# Aggregation pipeline to count customers by state
pipeline = [
    {"$group": {"_id": "$address.state", "customer_count": {"$sum": 1}}},
    {"$sort": {"customer_count": -1}}
]

# Execute the aggregation pipeline
results = db.customers.aggregate(pipeline)

# Print the results
for result in results:
    print(f"State: {result['_id']}, Count: {result['customer_count']}")
