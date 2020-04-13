from pymongo import MongoClient

__author__ = "Shubham Agrawal"

# MongoClient connects with default local host and port
myClient = MongoClient()

# Creates "mydb" if it does not exist
db = myClient.mydb

# Creates "users" collection if it does not exist
users = db.users

# Find the first document in the users collection
print(users.find_one())

# Return all documents in the "users" collection, and print each document
for x in users.find():
    print(x)

# Sort the result alphabetically by username
mydoc = users.find().sort("username")
# Sort the result reverse alphabetically by username
# mydoc = users.find().sort("username", -1)

for x in mydoc:
    print(x)

# Limit the result to only return 5 documents
myresult = users.find().limit(5)

for x in myresult:
    print(x)
