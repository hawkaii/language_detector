import time
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# You must set GOOGLE_API_KEY in your .env file
API_KEY = os.getenv("GOOGLE_API_KEY")

def detect_language(audio_file_path):
    start = time.time()
    try:
        if not API_KEY:
            raise ValueError("GOOGLE_API_KEY not set in environment.")
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel("gemini-pro")
        with open(audio_file_path, "rb") as f:
            audio_data = f.read()
        # Gemini API expects a prompt; we ask for language detection
        prompt = "What is the spoken language in this audio? Respond with only the language code (e.g., en, hi, ta, etc)."
        response = model.generate_content([
            prompt,
            genai.types.Blob(mime_type="audio/wav", data=audio_data)
        ])
        detected_language = response.text.strip().split()[0]  # crude extraction
        cost = 0.01  # Placeholder, update with real cost if available
        status = "success"
        error = None
    except Exception as e:
        detected_language = None
        cost = 0
        status = "error"
        error = str(e)
    end = time.time()
    return {
        "provider": "Google Gemini",
        "language": detected_language,
        "time_taken": round(end - start, 3),
        "cost": cost,
        "status": status,
        "error": error
    }
