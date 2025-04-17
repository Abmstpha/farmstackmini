import logging
from fastapi import APIRouter, Depends, HTTPException, status
from odmantic import ObjectId
from app.db.session import db 
from odmantic import ObjectId
from bson.errors import InvalidId

# from app.db.database import engine
from app.db.session import get_db

from app.models.note import Note
from app.services.auth import get_current_active_user
from app.schemas.user import User
from typing import List

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", response_model=Note, status_code=status.HTTP_201_CREATED)
async def create_note(note: Note, current_user: User = Depends(get_current_active_user)):
    note.username = current_user.username
    await db.engine.save(note)
    logger.info(f"Note created by {current_user.username}: {note.title}")
    return note


@router.get("/", response_model=List[Note])
async def get_user_notes(current_user=Depends(get_current_active_user)):
    notes = await db.engine.find(Note, Note.username == current_user.username)
    return notes


# @router.delete("/{note_id}")
# async def delete_note(note_id: str, current_user=Depends(get_current_active_user)):
#     note = await db.engine.find_one(Note, Note.id == note_id)

#     if not note:
#         raise HTTPException(status_code=404, detail="Note not found")
    
#     if note.username != current_user.username:
#         raise HTTPException(status_code=403, detail="Not authorized to delete this note")
    
#     await db.engine.delete(note)
#     return {"message": "Note deleted successfully"}


@router.delete("/{note_id}")
async def delete_note(note_id: str, current_user=Depends(get_current_active_user)):
    try:
        obj_id = ObjectId(note_id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid note ID format")

    note = await db.engine.find_one(Note, Note.id == obj_id)

    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    
    if note.username != current_user.username:
        raise HTTPException(status_code=403, detail="Not authorized to delete this note")
    
    await db.engine.delete(note)
    return {"message": "Note deleted successfully"}