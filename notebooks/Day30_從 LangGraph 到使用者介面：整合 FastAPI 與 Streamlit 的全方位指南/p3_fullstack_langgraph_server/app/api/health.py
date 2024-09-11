from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class HealthResponse(BaseModel):
    status: str

@router.get("/health", response_model=HealthResponse)
async def health_check():
    return {"status": "OK"}