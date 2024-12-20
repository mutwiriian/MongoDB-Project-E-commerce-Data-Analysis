from pymongo import MongoClient

client = MongoClient("mongodb://172.22.0.1:27017")

db = client["ecommerce"]

customers = db["customers"]

customers.create_index("customer_id")

products = db["products"]
products.create_index("product_id")

orders = db["orders"]
orders.create_index("customer_id")

order_items = db["order_items"]
order_items.create_index("order_id")

order_items.create_index("product_id")
