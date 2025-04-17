import logging
from typing import Annotated

from fastapi import APIRouter, Depends

from app.schemas.user import User
from app.services.auth import get_current_active_user

logger = logging.getLogger(__name__)
router = APIRouter()

@router.get("/me/", response_model=User)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)],
) -> User:
    logger.info(f"Profile information requested for user: {current_user.username}")
    return current_user

@router.get("/me/items/")
async def read_own_items(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    logger.info(f"Items requested for user: {current_user.username}")
    return [{"item_id": "Foo", "owner": current_user.username}] 