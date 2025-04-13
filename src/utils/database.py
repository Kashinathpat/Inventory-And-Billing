import os

from bson.objectid import ObjectId
from dotenv import load_dotenv
from pymongo import MongoClient, errors
from pymongo.synchronous.collection import Collection
from pymongo.synchronous.database import Database

load_dotenv()
mongo_uri = os.getenv("MONGO_URI")


class MongoDBClient:
    def __init__(self, uri: str, db_name: str):
        self.uri = uri
        self.db_name = db_name
        self.client: MongoDBClient | None = None
        self.db: Database | None = None
        self.inventory: Collection | None = None
        self.users: Collection | None = None
        self.connect()

    def connect(self):
        """Attempts to connect to MongoDB with retries."""
        try:
            self.client = MongoClient(self.uri, serverSelectionTimeoutMS=3000)
            self.db = self.client[self.db_name]
            self.inventory = self.db["inventory"]
            self.users = self.db["users"]
            print("Connected to MongoDB.")
            return
        except errors.PyMongoError as e:
            print(f"Connection attempt failed: {e}")

        print("Could not connect to MongoDB.")

    def check_login(self, username: str, password: str) -> str:
        """Checks if login credentials are valid."""
        if self.users is None:
            self.connect()
        try:
            user = self.users.find_one({"username": username.strip(), "password": password.strip()})
            return "" if user else "Invalid Username or Password.\nPlease check and try again."
        except errors.PyMongoError:
            return "Login failed due to Database error!\nCheck internet connection or try again later."

    def get_inventory(self) -> list | str:
        """Fetches inventory data."""
        if self.inventory is None:
            self.connect()
        try:
            return list(self.inventory.find())
        except errors.PyMongoError:
            return "Error fetching inventory data.\nCheck internet connection or try again later."

    def addItem(self, name: str, sku: str, price: float, stock: int) -> str:
        """Adds a new inventory item."""
        if self.inventory is None:
            self.connect()
        try:
            item = {"name": name, "sku": sku, "price": price, "stock": stock}
            self.inventory.insert_one(item)
            return ""
        except errors.PyMongoError:
            return f"Error adding item.\nCheck internet connection or try again later."

    def updateItem(self, _id: str, name: str, sku: str, price: float, stock: int) -> str:
        """Updates an existing item by ID."""
        if self.inventory is None:
            self.connect()
        try:
            self.inventory.update_one(
                {"_id": ObjectId(_id)},
                {"$set": {"name": name, "sku": sku, "price": price, "stock": stock}}
            )
            return ""
        except errors.PyMongoError:
            return f"Error updating item.\nCheck internet connection or try again later."

    def deleteItem(self, _id: str) -> str:
        """Deletes an item by ID."""
        if self.inventory is None:
            self.connect()
        try:
            self.inventory.delete_one({"_id": ObjectId(_id)})
            return ""
        except errors.PyMongoError:
            return f"Error deleting item.\nCheck internet connection or try again later."


mongo_client = MongoDBClient(mongo_uri, "Store")
