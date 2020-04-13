from pymongo import MongoClient

__author__ = "Shubham Agrawal"

# MongoClient connects with default local host and port
myClient = MongoClient()
# Another way to connect
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# Creates "mydb" if it does not exist
db = myClient.mydb
# Another way to choose DB
# db = myclient["mydb"]

# Return a list of your system's databases
print(myClient.list_database_names())

# Check if "mydatabase" exists:
dblist = myClient.list_database_names()
if "mydatabase" in dblist:
    print("My database exists.")

# Creates "users" collection if it does not exist
users = db.users
# Another way to create/get collection
# users = db["users"]

# Return a list of all collections in your database
print(db.list_collection_names())

# Check if the "users" collection exists
collectionList = db.list_collection_names()
if "users" in collectionList:
    print("Users collection exists.")

# Delete the "users" collection
# users.drop()
