from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine
from app.core.config import settings

class Database:
    client: AsyncIOMotorClient = None
    engine: AIOEngine = None

db = Database()

async def connect_to_mongo():
    try:
        db.client = AsyncIOMotorClient(settings.MONGODB_URI)
        db.engine = AIOEngine(client=db.client, database=settings.MONGODB_DB_NAME)
        print("✅ Connected to MongoDB with ODMantic")
    except Exception as e:
        print(f"❌ Failed to connect to MongoDB: {str(e)}")
        db.client = None
        db.engine = None

async def close_mongo_connection():
    if db.client:
        try:
            db.client.close()
            print("🔌 Closed MongoDB connection")
        except Exception as e:
            print(f"⚠️ Error closing MongoDB connection: {str(e)}")
    db.client = None
    db.engine = None

async def get_db():
    if db.engine is None:
        raise RuntimeError("Database not connected. Make sure connect_to_mongo() is called on startup.")
    return db.engine
