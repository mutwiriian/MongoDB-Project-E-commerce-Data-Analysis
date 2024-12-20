from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://172.22.0.1:27017/")
db = client["ecommerce"]

# Define validation schema
validation_schema = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["price"],
        "properties": {
            "price": {
                "bsonType": ["double", "int", "decimal"],
                "minimum": 0,
                "description": "The price must be a positive number."
            }
        }
    }
}

try:
    # Try to create the collection with schema validation
    db.create_collection(
        "products",
        validator=validation_schema
    )
    print("Schema applied to 'products' collection.")
except Exception as e:
    # If collection already exists, modify its schema
    if "collection products already exists" in str(e):
        db.command({
            "collMod": "products",
            "validator": validation_schema
        })
        print("Schema updated for 'products' collection.")
    else:
        print(f"Unexpected error: {e}")

#Test
db.products.insert_one({"product_name": "Widget", "price": 50})

db.products.insert_one({"product_name": "Widget", "price": -10})  # Negative price
db.products.insert_one({"product_name": "Widget"})               # Missing price
