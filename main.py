from fastapi import FastAPI
from routers import grammar, writing, listening, speaking, quiz

app = FastAPI(
    title="AI Belajar Inggris (Tutor Cerdas)",
    description="AI pembelajaran bahasa Inggris: grammar, writing, speaking, listening, dan quiz interaktif.",
    version="2.0.0"
)

app.include_router(grammar.router, prefix="/ai", tags=["Grammar"])
app.include_router(writing.router, prefix="/ai", tags=["Writing"])
app.include_router(speaking.router, prefix="/ai", tags=["Speaking"])
app.include_router(listening.router, prefix="/ai", tags=["Listening"])
app.include_router(quiz.router, prefix="/ai", tags=["Quiz"])

@app.get("/")
def root():
    return {
        "message": "✨ Tutor AI Bahasa Inggris aktif!",
        "fitur": ["/ai/grammar", "/ai/writing", "/ai/speaking", "/ai/listening", "/ai/quiz"]
    }
