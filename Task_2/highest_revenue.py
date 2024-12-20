from pymongo import MongoClient

client = MongoClient("mongodb://172.22.0.1:27017") 
db = client["ecommerce"] 


pipeline = [
    {
        "$lookup": {
            "from": "products",
            "localField": "product_id",
            "foreignField": "product_id",
            "as": "product_details"
        }
    },
    {
        "$unwind": "$product_details"
    },
    {
        "$project": {
            "_id": 0,
            "category": "$product_details.category",
            "revenue": {"$multiply": ["$quantity", "$price"]} 
        }
    },
    {
        "$group": {
            "_id": "$category",
            "total_revenue": {"$sum": "$revenue"}
        }
    },
    {
        "$sort": {"total_revenue": -1} 
    }
]

results = db.order_items.aggregate(pipeline)

for result in results:
    print(f"Category: {result['_id']}, Total Revenue: {result['total_revenue']}")
