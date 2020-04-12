import datetime

import pymongo
from pymongo import MongoClient

__author__ = "Shubham Agrawal"

myClient = MongoClient()
db = myClient.mydb
users = db.users

# Creating an index (usually required for scalability purposes)
users.create_index([("username", pymongo.ASCENDING)], unique=True)

# insert one
user1 = {"username": "s", "password": "secure_password", "fav_number": 7, "hobbies": ["technology", "philately"]}
user_id = users.insert_one(user1).inserted_id

# insert many
many_users = [{"username": "s1", "password": "12345"}, {"username": "s2", "password": "67890"}]
inserted = users.insert_many(many_users)

# another way to insert
cur_date = datetime.datetime.now()
# inserted = users.insert({"username": "s3", "date": cur_date})
