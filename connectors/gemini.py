import time
import os
import google.generativeai as genai
from google.generativeai.protos import Blob
from dotenv import load_dotenv

load_dotenv()

# You must set GEMINI_API_KEY in your .env file
API_KEY = os.getenv("GEMINI_API_KEY")

def detect_language(audio_file_path):
    start = time.time()
    try:
        if not API_KEY:
            raise ValueError("GEMINI_API_KEY not set in environment.")
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel("gemini-1.5-flash")
        with open(audio_file_path, "rb") as f:
            audio_data = f.read()
        prompt = "What is the spoken language in this audio? Respond with only the language code (e.g., en, hi, ta, etc)."
        # Create a proper Blob object for audio data
        audio_blob = Blob(mime_type="audio/wav", data=audio_data)
        response = model.generate_content([
            prompt,
            audio_blob
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
