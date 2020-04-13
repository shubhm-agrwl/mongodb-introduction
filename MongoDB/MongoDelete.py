from pymongo import MongoClient

__author__ = "Shubham Agrawal"

# MongoClient connects with default local host and port
myClient = MongoClient()

# Creates "mydb" if it does not exist
db = myClient.mydb

# Creates "users" collection if it does not exist
users = db.users

# Delete the document with the username "s"
myquery = {"username": "s"}
users.delete_one(myquery)

# Delete all documents were the username starts with the letter S:
myquery = {"username": {"$regex": "^S"}}
x = users.delete_many(myquery)
print(x.deleted_count, " documents deleted.")

# Delete all documents in the "users" collection
x = users.delete_many({})
print(x.deleted_count, " documents deleted.")
