import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Model yang digunakan
model = genai.GenerativeModel("gemini-2.0-flash")


# Fungsi umum untuk panggil model Gemini
def ask_gemini(prompt: str):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Error dari Gemini: {str(e)}"


# === 1️⃣ Writing Feedback ===
def writing_feedback(text: str):
    prompt = f"""
You are an expert English writing tutor.
Analyze this text carefully and provide feedback.

Please include:
1. Corrected version (in English)
2. Detailed feedback in English
3. The same feedback explained again in **Bahasa Indonesia** so the learner can understand easily.
4. Tips to make the writing sound more natural.

Text to analyze:
{text}
"""
    return ask_gemini(prompt)


# === 2️⃣ Grammar Check ===
def grammar_check(text: str):
    prompt = f"""
You are a professional English grammar teacher.
Correct the grammar and explain all mistakes.

Include:
1. Corrected sentence (in English)
2. Explanation of each grammar error (in English)
3. The same explanation translated and explained again in **Bahasa Indonesia** clearly.

Text:
{text}
"""
    return ask_gemini(prompt)


# === 3️⃣ Speaking Tips ===
def speaking_tips(text: str):
    prompt = f"""
You are an English pronunciation and speaking coach.
Provide a detailed pronunciation guide and tone explanation.

Include:
1. Phonetic pronunciation (IPA)
2. 3 pronunciation tips (in English)
3. Example sentence with correct tone or stress
4. Explanation in **Bahasa Indonesia** about how to pronounce and intonate correctly.

Sentence:
{text}
"""
    return ask_gemini(prompt)


# === 4️⃣ Listening Practice ===
def listening_practice(level: str):
    prompt = f"""
You are an English listening teacher.
Generate one short listening exercise suitable for {level} learners.

Include:
1. Transcript (in English, 2–4 sentences)
2. 3 comprehension questions (A–D)
3. Answer key
4. Short summary and translation in **Bahasa Indonesia** to help learners understand.

Level: {level}
"""
    return ask_gemini(prompt)


# === 5️⃣ Quiz Generator ===
def generate_quiz(topic: str, level: str):
    prompt = f"""
You are an English quiz generator.
Create 5 multiple-choice questions (A–D) about "{topic}" for {level} learners.

Include:
1. Each question and choices (in English)
2. Correct answers at the end
3. A brief explanation and translation in **Bahasa Indonesia** for each question and answer.

Topic: {topic}
Level: {level}
"""
    return ask_gemini(prompt)
