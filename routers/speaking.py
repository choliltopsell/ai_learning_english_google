from fastapi import APIRouter, Body
from services.gemini_service import speaking_tips

router = APIRouter()

@router.post("/speaking")
def speaking_guide(data: dict = Body(...)):
    text = data.get("text", "")
    if not text:
        return {"error": "Masukkan kalimat bahasa Inggris."}
    return {"result": speaking_tips(text)}
