import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from app.core.config import settings
from app.routers import api_router
from app.db.session import connect_to_mongo, close_mongo_connection

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        logger.info("Starting up application")
        await connect_to_mongo()
        logger.info("Connected to MongoDB")
        yield
        await close_mongo_connection()
        logger.info("MongoDB connection closed")
    except Exception as e:
        logger.error(f"Startup error: {str(e)}")
        raise

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    lifespan=lifespan
)

app.include_router(api_router)
