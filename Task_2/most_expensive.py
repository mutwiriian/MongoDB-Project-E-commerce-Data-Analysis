from pymongo import MongoClient

client = MongoClient("mongodb://172.22.0.1/27017")
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
        "$group": {
            "_id": "$order_id",
            "top_products": {
                "$push": {
                    "product_name": "$product_details.product_name",
                    "price": "$price",
                    "quantity": "$quantity"
                }
            }
        }
    },
    {
        "$project": {
            "top_products": {
                "$slice": [
                    {
                        "$sortArray": {
                            "input": "$top_products",
                            "sortBy": { "price": -1 }
                        }
                    },
                    3
                ]
            }
        }
    },
    {
        "$sort": { "_id": -1 }
    }
]

result = db["order_items"].aggregate(pipeline)

for order in result:
    print(f"Order ID: {order['_id']}")
    for product in order["top_products"]:
        print(f"  - Product: {product['product_name']}, Price: {product['price']}, Quantity: {product['quantity']}")
