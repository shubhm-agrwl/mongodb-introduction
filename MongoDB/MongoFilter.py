import datetime

from pymongo import MongoClient

__author__ = "Shubham Agrawal"

# MongoClient connects with default local host and port
myClient = MongoClient()

# Creates "mydb" if it does not exist
db = myClient.mydb

# Creates "users" collection if it does not exist
users = db.users

# Count number of documents
print(users.find().count())

# Count based on one filter
print(users.find({"fav_number": 7}).count())

# Count based on many filters
print(users.find({"fav_number": 7, "username": "s"}).count())

# Count documents which are after the old date
old_date = datetime.datetime(2019, 1, 1)
print(users.find({"date": {"$gte": old_date}}).count())

# Count documents which are before the old date
print(users.find({"date": {"$lt": old_date}}).count())

# Count documents where "date" field exists
print(users.find({"date": {"$exists": True}}).count())

# Count documents where "username" not equal to "s"
print(users.find({"username": {"$ne": "s"}}).count())
