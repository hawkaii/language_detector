import time

from utils import get_audio_duration, estimate_cost
import time
import os
import openai

def detect_language(audio_file_path):
    start = time.time()
    try:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable is not set")
        openai.api_key = api_key
        with open(audio_file_path, "rb") as audio_file:
            response = openai.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
                response_format="json",
                language=None,  # Let Whisper auto-detect
                timestamp_granularities=["segment"]
            )
        detected_language = response.get("language", "unknown")
        duration_sec = get_audio_duration(audio_file_path)
        cost = estimate_cost("OpenAI", duration_sec)
        status = "success"
        error = None
    except Exception as e:
        detected_language = None
        cost = 0
        status = "error"
        error = str(e)
    end = time.time()
    return {
        "provider": "OpenAI",
        "language": detected_language,
        "time_taken": round(end - start, 3),
        "cost": cost,
        "status": status,
        "error": error
    }

