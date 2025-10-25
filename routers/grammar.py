from fastapi import APIRouter, Body
from services.gemini_service import grammar_check

router = APIRouter()

@router.post("/grammar")
def grammar_check_api(data: dict = Body(...)):
    text = data.get("text", "")
    if not text:
        return {"error": "Masukkan teks yang ingin diperiksa."}
    return {"result": grammar_check(text)}
