import os
import time
import requests

def detect_language(audio_file_path):
    start = time.time()
    try:
        api_key = os.getenv("SARVAM_API_KEY")
        if not api_key:
            raise ValueError("SARVAM_API_KEY environment variable is not set")
        url = "https://api.sarvam.ai/speech-to-text"
        headers = {
            "api-subscription-key": api_key
        }
        with open(audio_file_path, "rb") as audio_file:
            files = {"file": (os.path.basename(audio_file_path), audio_file, "audio/wav")}
            response = requests.post(url, headers=headers, files=files)
            response.raise_for_status()
            result = response.json()
            # Try to extract language from the response
            detected_language = result.get("language", result.get("language_code", "unknown"))
            cost = 0.01  # Placeholder for cost, update if pricing is known
            status = "success"
            error = None
    except Exception as e:
        detected_language = "unknown"
        cost = 0
        status = "error"
        error = str(e)
    end = time.time()
    return {
        "provider": "Sarvam AI",
        "language": detected_language,
        "time_taken": round(end - start, 3),
        "cost": cost,
        "status": status,
        "error": error
    }
