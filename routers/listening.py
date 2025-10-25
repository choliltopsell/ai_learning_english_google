from fastapi import APIRouter, Body
from services.gemini_service import listening_practice

router = APIRouter()

@router.post("/listening")
def listening_exercise(data: dict = Body(...)):
    level = data.get("level", "beginner")
    return {"level": level, "result": listening_practice(level)}
