from pymongo import MongoClient
from pymongo.errors import PyMongoError

# Connect to MongoDB
client = MongoClient("mongodb://172.22.0.1:27017/?replicaSet=rs0")
db = client["shop"]

# Collections
orders = db["orders"]
inventory = db["inventory"]

# Simulated Order Data
order_data = {
    "order_id": 1,
    "customer_id": 101,
    "items": [
        {"product_id": 201, "quantity": 2},
        {"product_id": 202, "quantity": 1}
    ],
    "status": "Pending"
}

# Function to process an order atomically
def create_order(order):
    # Start a session
    with client.start_session() as session:
        try:
            # Start a transaction
            with session.start_transaction():
                # Insert the order into the orders collection
                orders.insert_one(order, session=session)

                # Update inventory for each item in the order
                for item in order["items"]:
                    inventory.update_one(
                        {"product_id": item["product_id"]},
                        {"$inc": {"stock": -item["quantity"]}},
                        session=session
                    )
                print("Transaction committed successfully.")

        except PyMongoError as e:
            print(f"Transaction aborted due to error: {e}")

# Simulate the order creation
create_order(order_data)
