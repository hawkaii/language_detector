import os
import time
import requests

from utils import get_audio_duration, estimate_cost
import os
import time
import requests

def detect_language(audio_file_path):
    start = time.time()
    
    try:
        api_key = os.getenv("ELEVENLABS_API_KEY")
        if not api_key:
            raise ValueError("ELEVENLABS_API_KEY environment variable is not set")
        
        url = "https://api.elevenlabs.io/v1/speech-to-text"
        
        headers = {
            "xi-api-key": api_key
        }
        
        data = {
            "model_id": "scribe_v1"
        }
        
        with open(audio_file_path, "rb") as audio_file:
            files = {
                "file": audio_file
            }
            
            response = requests.post(url, headers=headers, data=data, files=files)
            response.raise_for_status()
            
            result = response.json()
            detected_language = result.get("language_code", "unknown")
            duration_sec = get_audio_duration(audio_file_path)
            cost = estimate_cost("ElevenLabs", duration_sec)
            
            status = "success"
            error = None
            
    except Exception as e:
        detected_language = "unknown"
        cost = 0
        status = "error"
        error = str(e)
    
    end = time.time()
    return {
        "provider": "ElevenLabs",
        "language": detected_language,
        "time_taken": round(end - start, 3),
        "cost": cost,
        "status": status,
        "error": error
    }

