from pymongo import MongoClient

client = MongoClient("mongodb://172.22.0.1/27017")

db = client["ecommerce"]

customers = db["customers"]

customers.insert_many(
[
  {
    "customer_id": 14,
    "name": "Donia",
    "email": "dadamides0@naver.com",
    "address": {
      "street": "94 Dunning Park",
      "city": "Ayna",
      "state": "CA"
    }
  },
  {
    "customer_id": 12,
    "name": "Gearard",
    "email": "gwennam1@typepad.com",
    "address": {
      "street": "4121 Coolidge Plaza",
      "city": "Nglengkong",
      "state": "ID"
    }
  },
  {
    "customer_id": 3,
    "name": "Sharron",
    "email": "sreppaport2@auda.org.au",
    "address": {
      "street": "4648 Eagle Crest Crossing",
      "city": "Estombar",
      "state": "TX"
    }
  },
  {
    "customer_id": 5,
    "name": "Margi",
    "email": "mbonavia3@technorati.com",
    "address": {
      "street": "970 Russell Place",
      "city": "Podhum",
      "state": "NY"
    }
  },
  {
    "customer_id": 17,
    "name": "Madge",
    "email": "mcuthbert4@geocities.jp",
    "address": {
      "street": "1 Bultman Way",
      "city": "Pithoro",
      "state": "CA" 
    }
  },
  {
    "customer_id": 2,
    "name": "Bax",
    "email": "bdashkov5@weather.com",
    "address": {
      "street": "882 Thompson Parkway",
      "city": "Tempeh Tengah",
      "state": "TX"
    }
  },
  {
    "customer_id": 16,
    "name": "Laina",
    "email": "lgrimsditch6@reverbnation.com",
    "address": {
      "street": "4345 Nancy Hill",
      "city": "Žabčice",
      "state": "CA" 
    }
  },
  {
    "customer_id": 13,
    "name": "Ursola",
    "email": "udabell7@telegraph.co.uk",
    "address": {
      "street": "975 Mosinee Hill",
      "city": "Columbus",
      "state": "GA"
    }
  },
  {
    "customer_id": 10,
    "name": "Zena",
    "email": "zrobarts8@blog.com",
    "address": {
      "street": "2 Forest Crossing",
      "city": "Kunmi Erdi",
      "state": "FL" 
    }
  },
  {
    "customer_id": 18,
    "name": "Ronnica",
    "email": "rlathbury9@woothemes.com",
    "address": {
      "street": "303 Golf View Plaza",
      "city": "Feitoria",
      "state": "FL"
    }
  },
  {
    "customer_id": 11,
    "name": "Delainey",
    "email": "dcristoforettia@arstechnica.com",
    "address": {
      "street": "7455 Ludington Plaza",
      "city": "Looc",
      "state": "NY" 
    }
  },
  {
    "customer_id": 4,
    "name": "Lonny",
    "email": "lvenningb@usda.gov",
    "address": {
      "street": "303 Del Sol Court",
      "city": "Pakisrejo",
      "state": "CA" 
    }
  },
  {
    "customer_id": 20,
    "name": "Abie",
    "email": "asaunierec@amazon.co.uk",
    "address": {
      "street": "62 Vernon Pass",
      "city": "Novosmolinskiy",
      "state": "NY" 
    }
  },
  {
    "customer_id": 15,
    "name": "Revkah",
    "email": "rjolleyd@usgs.gov",
    "address": {
      "street": "5088 Ridgeway Avenue",
      "city": "Casalinho",
      "state": "FL" 
    }
  },
  {
    "customer_id": 9,
    "name": "Parry",
    "email": "pcockshotte@ucsd.edu",
    "address": {
      "street": "77626 Hovde Park",
      "city": "Maragogi",
      "state": "CA" 
    }
  },
  {
    "customer_id": 6,
    "name": "Jemie",
    "email": "jpinef@yolasite.com",
    "address": {
      "street": "2 Gulseth Parkway",
      "city": "Malata",
      "state": "TX" 
    }
  },
  {
    "customer_id": 19,
    "name": "Sarette",
    "email": "sbundyg@mayoclinic.com",
    "address": {
      "street": "343 Boyd Circle",
      "city": "Ilare",
      "state": "NY" 
    }
  },
  {
    "customer_id": 7,
    "name": "Clarine",
    "email": "cchiezeh@columbia.edu",
    "address": {
      "street": "7 Prairieview Crossing",
      "city": "Cirumput",
      "state": "FL" 
    }
  },
  {
    "customer_id": 1,
    "name": "Sal",
    "email": "saldinsi@comcast.net",
    "address": {
      "street": "34 Saint Paul Crossing",
      "city": "Niedercorn",
      "state": "CA" 
    }
  },
  {
    "customer_id": 8,
    "name": "Juliet",
    "email": "jblockj@spiegel.de",
    "address": {
      "street": "0353 Twin Pines Avenue",
      "city": "Molde",
      "state": "GA"
    }
  }
]
)

products = db["products"]

products.insert_many(
[{
  "product_id": 121,
  "product_name": "Wooden Stool",
  "category": "Furniture",
  "price": 1129
}, {
  "product_id": 109,
  "product_name": "Remote Controller",
  "category": "Electronics",
  "price": 1294
}, {
  "product_id": 130,
  "product_name": "Mouse Pad",
  "category": "Accesories",
  "price": 948
}, {
  "product_id": 108,
  "product_name": "HiFi Speakers",
  "category": "Electronics",
  "price": 1149
}, {
  "product_id": 107,
  "product_name": "Cooling Fan",
  "category": "Accesories",
  "price": 1209
}, {
  "product_id": 113,
  "product_name": "Jeans Trousers",
  "category": "Clothes",
  "price": 1379
}, {
  "product_id": 118,
  "product_name": "LCD Monitor",
  "category": "Electronics",
  "price": 923
}, {
  "product_id": 120,
  "product_name": "Dining Table",
  "category": "Furniture",
  "price": 1069
}, {
  "product_id": 101,
  "product_name": "Sweat Shirt",
  "category": "Clothes",
  "price": 1107
}, {
  "product_id": 114,
  "product_name": "Electic Kettle",
  "category": "Electronics",
  "price": 1071
}, {
  "product_id": 105,
  "product_name": "Fanta Orange",
  "category": "Drinks",
  "price": 1238
}, {
  "product_id": 101,
  "product_name": "Portable Hard Disk",
  "category": "Accesories",
  "price": 1147
}, {
  "product_id": 121,
  "product_name": "Office Desk",
  "category": "Furniture",
  "price": 1094
}, {
  "product_id": 126,
  "product_name": "Earphones",
  "category": "Accesories",
  "price": 948
}, {
  "product_id": 110,
  "product_name": "Chocolate Bar - Coffee Crisp",
  "category": "Drinks",
  "price": 1274
}, {
  "product_id": 124,
  "product_name": "Laptop",
  "category": "Electronics",
  "price": 1271
}, {
  "product_id": 112,
  "product_name": "Hot Chocolate - Individual",
  "category": "Drinks",
  "price": 1084
}, {
  "product_id": 126,
  "product_name": "Socks",
  "category": "Clothes",
  "price": 1103
}, {
  "product_id": 122,
  "product_name": "Adjustable Desk",
  "category": "Furniture",
  "price": 1163
}, {
  "product_id": 119,
  "product_name": "Crop Top",
  "category": "Clothes",
  "price": 927
}]
)

orders = db["orders"]

orders.insert_many(
[
  {
    "order_id": 5011,
    "customer_id": 1,
    "order_date": "2024-10-22",
    "status": "Delivered",
    "delivery_date": "2024-10-25" 
  },
  {
    "order_id": 5000,
    "customer_id": 12,
    "order_date": "2024-03-14",
    "status": "Not Delivered"
  },
  {
    "order_id": 5026,
    "customer_id": 8,
    "order_date": "2024-09-10",
    "status": "Delivered",
    "delivery_date": "2024-09-13" 
  },
  {
    "order_id": 5301,
    "customer_id": 11,
    "order_date": "2024-02-16",
    "status": "Delivered",
    "delivery_date": "2024-02-19" 
  },
  {
    "order_id": 5351,
    "customer_id": 5,
    "order_date": "2024-05-21",
    "status": "Delivered",
    "delivery_date": "2024-05-24" 
  },
  {
    "order_id": 5391,
    "customer_id": 16,
    "order_date": "2024-06-11",
    "status": "Delivered",
    "delivery_date": "2024-06-15" 
  },
  {
    "order_id": 5871,
    "customer_id": 14,
    "order_date": "2024-07-22",
    "status": "In Transit"
  },
  {
    "order_id": 5911,
    "customer_id": 18,
    "order_date": "2024-11-22",
    "status": "Not Delivered"
  },
  {
    "order_id": 5140,
    "customer_id": 17,
    "order_date": "2024-11-23",
    "status": "Delivered",
    "delivery_date": "2024-11-26" 
  },
  {
    "order_id": 5001,
    "customer_id": 6,
    "order_date": "2024-10-15",
    "status": "Delivered",
    "delivery_date": "2024-10-18" 
  },
  {
    "order_id": 5551,
    "customer_id": 5,
    "order_date": "2024-04-25",
    "status": "In Transit"
  },
  {
    "order_id": 5781,
    "customer_id": 10,
    "order_date": "2024-09-03",
    "status": "Delivered",
    "delivery_date": "2024-09-06" 
  },
  {
    "order_id": 5151,
    "customer_id": 16,
    "order_date": "2024-04-14",
    "status": "Not Delivered"
  },
  {
    "order_id": 5456,
    "customer_id": 13,
    "order_date": "2024-12-14",
    "status": "Not Delivered"
  },
  {
    "order_id": 6531,
    "customer_id": 14,
    "order_date": "2024-09-05",
    "status": "Delivered",
    "delivery_date": "2024-09-08" 
  },
  {
    "order_id": 4601,
    "customer_id": 12,
    "order_date": "2024-07-14",
    "status": "Not Delivered"
  },
  {
    "order_id": 7841,
    "customer_id": 6,
    "order_date": "2024-06-01",
    "status": "In Transit"
  },
  {
    "order_id": 2734,
    "customer_id": 8,
    "order_date": "2024-01-17",
    "status": "Delivered",
    "delivery_date": "2024-01-20" 
  },
  {
    "order_id": 5891,
    "customer_id": 5,
    "order_date": "2024-10-08",
    "status": "Delivered",
    "delivery_date": "2024-10-11" 
  }
])

order_items = db["order_items"]

order_items.insert_many(

[
  {
    "order_item_id": 9001,
    "order_id": 5011,
    "product_id": 109,
    "quantity": 3,
    "price": 3882
  },
  {
    "order_item_id": 9002,
    "order_id": 5301,
    "product_id": 121,
    "quantity": 1,
    "price": 1129
  },
  {
    "order_item_id": 9003,
    "order_id": 5000,
    "product_id": 130,
    "quantity": 2,
    "price": 1896
  },
  {
    "order_item_id": 9004,
    "order_id": 5026,
    "product_id": 108,
    "quantity": 4,
    "price": 4596
  },
  {
    "order_item_id": 9005,
    "order_id": 5301,
    "product_id": 107,
    "quantity": 2,
    "price": 2418
  },
  {
    "order_item_id": 9006,
    "order_id": 5351,
    "product_id": 113,
    "quantity": 1,
    "price": 1379
  },
  {
    "order_item_id": 9007,
    "order_id": 5391,
    "product_id": 118,
    "quantity": 3,
    "price": 2769
  },
  {
    "order_item_id": 9008,
    "order_id": 5871,
    "product_id": 120,
    "quantity": 2,
    "price": 2138
  },
  {
    "order_item_id": 9009,
    "order_id": 5911,
    "product_id": 101,
    "quantity": 4,
    "price": 4428
  },
  {
    "order_item_id": 9010,
    "order_id": 5140,
    "product_id": 114,
    "quantity": 1,
    "price": 1071
  },
  {
    "order_item_id": 9011,
    "order_id": 5001,
    "product_id": 105,
    "quantity": 3,
    "price": 3714
  },
  {
    "order_item_id": 9012,
    "order_id": 5551,
    "product_id": 101,
    "quantity": 2,
    "price": 2214
  },
  {
    "order_item_id": 9013,
    "order_id": 5781,
    "product_id": 121,
    "quantity": 1,
    "price": 1129
  },
  {
    "order_item_id": 9014,
    "order_id": 5151,
    "product_id": 126,
    "quantity": 5,
    "price": 4740
  },
  {
    "order_item_id": 9015,
    "order_id": 5456,
    "product_id": 110,
    "quantity": 2,
    "price": 2548
  },
  {
    "order_item_id": 9016,
    "order_id": 6531,
    "product_id": 124,
    "quantity": 1,
    "price": 1271
  },
  {
    "order_item_id": 9017,
    "order_id": 4601,
    "product_id": 112,
    "quantity": 4,
    "price": 4336
  },
  {
    "order_item_id": 9018,
    "order_id": 7841,
    "product_id": 126,
    "quantity": 3,
    "price": 2844
  },
  {
    "order_item_id": 9019,
    "order_id": 2734,
    "product_id": 119,
    "quantity": 2,
    "price": 1854
  },
  {
    "order_item_id": 9020,
    "order_id": 5891,
    "product_id": 122,
    "quantity": 1,
    "price": 1163
  }
]
)
