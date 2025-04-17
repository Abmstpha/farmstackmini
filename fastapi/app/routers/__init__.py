# app/routers/__init__.py

from fastapi import APIRouter

from .auth import router as auth_router
from .notes import router as notes_router
from .users import router as users_router
from .health import router as health_router

api_router = APIRouter()
api_router.include_router(auth_router, tags=["auth"])
api_router.include_router(users_router, prefix="/users", tags=["users"])
api_router.include_router(notes_router, prefix="/notes", tags=["notes"])
api_router.include_router(health_router, prefix="/health", tags=["health"])
