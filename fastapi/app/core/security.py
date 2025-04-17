from datetime import datetime, timedelta, timezone
import logging

from passlib.context import CryptContext
import jwt

from app.core.config import settings

logger = logging.getLogger(__name__)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    logger.info("Verifying password for authentication attempt")
    is_valid = pwd_context.verify(plain_password, hashed_password)
    logger.info(f"Password verification result: {'success' if is_valid else 'failed'}")
    return is_valid

def get_password_hash(password: str) -> str:
    logger.info("Generating password hash")
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    logger.info("Starting access token creation process")
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    logger.info(f"Creating JWT token with expiration: {expire}")
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    logger.info("JWT token created successfully")
    return encoded_jwt 