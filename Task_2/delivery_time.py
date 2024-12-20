from pymongo import MongoClient
from datetime import datetime

# Connect to MongoDB
client = MongoClient("mongodb://172.22.0.1:27017") 
db = client["ecommerce"] 

# Aggregation pipeline to calculate average delivery time for delivered orders
pipeline = [
    {
        "$match": {
            "status": "Delivered" 
        }
    },
    {
        "$addFields": {
            "order_date": {"$toDate": "$order_date"}, 
            "delivery_date": {"$toDate": "$delivery_date"} 
        }
    },
    {
        "$project": {
            "delivery_time": {
                "$subtract": [
                    "$delivery_date",
                    "$order_date"
                ]
            }
        }
    },
    {
        "$group": {
            "_id": None, 
            "avg_delivery_time": {"$avg": {"$divide": ["$delivery_time", 1000 * 60 * 60 * 24]}} 
        }
    }
]

# Execute the aggregation pipeline
results = db.orders.aggregate(pipeline)

# Print the average delivery time
for result in results:
    print(f"Average Delivery Time for Delivered Orders: {result['avg_delivery_time']:.2f} days")
