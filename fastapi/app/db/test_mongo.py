from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# 🔐 Insert your actual connection string below
uri = "mongodb+srv://abbenasm:tmPL0CAAs5yqUYAe@abducluster.8erj2yn.mongodb.net/?retryWrites=true&w=majority&appName=AbduCluster"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Ping to confirm
try:
    client.admin.command('ping')
    print("✅ Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("❌ Connection error:", e)
