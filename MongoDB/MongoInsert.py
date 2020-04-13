import datetime

import pymongo
from pymongo import MongoClient

__author__ = "Shubham Agrawal"

# MongoClient connects with default local host and port
myClient = MongoClient()

# Creates "mydb" if it does not exist
db = myClient.mydb

# Creates "users" collection if it does not exist
users = db.users

# Creating an index (usually required for scalability purposes)
users.create_index([("username", pymongo.ASCENDING)], unique=True)

# insert one
user1 = {"username": "s", "password": "secure_password", "fav_number": 7, "hobbies": ["technology", "philately"]}
inserted = users.insert_one(user1)

# Prints the value of the _id field
print(inserted.inserted_id)

# insert many
many_users = [{"username": "s1", "password": "12345"}, {"username": "s2", "password": "67890"}]
inserted = users.insert_many(many_users)

# Prints the value of the _id fields of the inserted documents
print(inserted.inserted_ids)

# another way to insert
cur_date = datetime.datetime.now()
inserted = users.insert({"username": "s3", "date": cur_date})
