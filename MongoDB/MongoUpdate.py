from pymongo import MongoClient

__author__ = "Shubham Agrawal"

# MongoClient connects with default local host and port
myClient = MongoClient()

# Creates "mydb" if it does not exist
db = myClient.mydb

# Creates "users" collection if it does not exist
users = db.users

# Change the username from "s" to "a":
myquery = {"username": "s"}
newvalues = {"$set": {"username": "a"}}
users.update_one(myquery, newvalues)

# print "users" after the update:
for x in users.find():
    print(x)

# Update all documents where the username starts with the letter "S":
myquery = {"username": {"$regex": "^S"}}
newvalues = {"$set": {"name": "a"}}
x = users.update_many(myquery, newvalues)
print(x.modified_count, "documents updated.")
