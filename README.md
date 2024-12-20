# MongoDB Design and Analysis for an E-commerce Platform
This project demonstrates the design of a NOSQL schema for an e-commerce platform and simple 
analytics for insights. The project is split into 4 tasks which are self-sufficient in the
sense that the results extracted or connections established in one script are independent of 
the other scripts. The database installation is local but can be easily extended to a managed 
cloud instance by changing the connection string

## Running scripts
To run a particular script, say `script.py`,  in any of the sub-folders, assuming a Linux environment, proceed as
follows:
First migrate into the project directory and activate the environment with
```
source .venv/bin/activate
```
Then install the required dependencies
```
pip install -r requirements.txt
```
To run a script execute the following in the terminal
```
python script.py
```

## Task 1
Within `../Task_1/`, `connect.py` runs a test connection to ensure connectivity and availability of the database
`create_data.py` inserts 20 documents in each collection in the `ecommerce` database.

## Task 2
`../Task_2/highest_revenue.py` runs a pipeline on the `products` collection to group and calculate revenue by category
The `../Task_2/delivery_time.py` script applies aggregation and joins to calculate the average delivery time for all
orders that were successfully delivered
In `../Task_2/highest_customers.py`, the number of customers in each state are counted using a grouping aggregation
and finally sorted in descending order
`../Task_2/most_expensive.py` applies a lookup aggregation and multiple joins to compute a the most expensive products
in each order

## Task 3
The choice between embedded and referenced schema designs depends on how related data is stored. In principle, data 
that is accessed together should be stored together to reduce the computational costs by queries that would otherwise
access multiple collections. In the  `customers` collection, the `address` field needs to be embedded in order to ensure
efficiency of queries. The other collections, i.e, `orders`, `products` and `order_items` use referenced schemas that 
guarantees consistency of orders and stock products. 

The `indices.py` script creates indices for the commonly used fields across all the collections

## Task 4
The `../Task_4/transaction.py` scripts simulates a safe order creations process in the database. 
`../Task_4/change_stream.py` simulates the tracking and logging of changes that occures for activities like order creation
and product upgrade
`../Task_4/schema_validation.py` applies a schema for new data data entered in the database and finally tests for their
validity by running true and false test


