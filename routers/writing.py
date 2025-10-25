from fastapi import APIRouter, Body
from services.gemini_service import writing_feedback

router = APIRouter()

@router.post("/writing")
def writing_check(data: dict = Body(...)):
    text = data.get("text", "")
    if not text:
        return {"error": "Masukkan teks bahasa Inggris yang ingin diperiksa."}
    return {"result": writing_feedback(text)}
