from fastapi import HTTPException
from fastapi import status

def health_check():
    try:
        return {"status": "ok"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
