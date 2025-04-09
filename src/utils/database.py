import os

from bson.objectid import ObjectId
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
mongo_uri = os.getenv("MONGO_URI")

client = MongoClient(mongo_uri)
db = client["Store"]
collection = db["inventory"]
userCollection = db["users"]

def check_login(username: str, password: str) -> str:
    user = userCollection.find_one({"username": username.strip(), "password": password.strip()})
    if user:
        return ""
    return "Invalid Username or Password.\nPlease check username and password and try again."

def getInventoryData():
  return list(collection.find())

def addItem(name: str, sku: str, price: float, stock: int):
    item = {
      "name": name,
      "sku": sku,
      "price": price,
      "stock": stock
    }
    result = collection.insert_one(item)
    return str(result.inserted_id)


def updateItem(_id: str, name: str, sku: str, price: float, stock: int):
  result = collection.update_one(
    {"_id": ObjectId(_id)},
    {"$set": {
      "name": name,
      "sku": sku,
      "price": price,
      "stock": stock
    }}
  )
  return result.modified_count

def deleteItem(_id: str):
    result = collection.delete_one({"_id": ObjectId(_id)})
    return result.deleted_count
