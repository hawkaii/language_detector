import time

def detect_language(audio_file_path):
    start = time.time()
    # Mocked response
    detected_language = "ta"
    cost = 0
    status = "success"
    error = None
    end = time.time()
    return {
        "provider": "Sarvam AI",
        "language": detected_language,
        "time_taken": round(end - start, 3),
        "cost": cost,
        "status": status,
        "error": error
    }
