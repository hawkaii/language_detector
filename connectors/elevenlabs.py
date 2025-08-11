import time

def detect_language(audio_file_path):
    start = time.time()
    # Mocked response
    detected_language = "en"
    cost = 0
    status = "success"
    error = None
    end = time.time()
    return {
        "provider": "ElevenLabs",
        "language": detected_language,
        "time_taken": round(end - start, 3),
        "cost": cost,
        "status": status,
        "error": error
    }
