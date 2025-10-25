from fastapi import APIRouter, Body
from services.gemini_service import generate_quiz

router = APIRouter()

@router.post("/quiz")
def quiz(data: dict = Body(...)):
    topic = data.get("topic", "")
    level = data.get("level", "intermediate")
    if not topic:
        return {"error": "Masukkan topik kuis."}
    return {"quiz": generate_quiz(topic, level)}
