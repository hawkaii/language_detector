import time
from contextlib import contextmanager

@contextmanager
def timer():
    start = time.time()
    yield lambda: round(time.time() - start, 3)

def safe_call(func, *args, **kwargs):
    try:
        return func(*args, **kwargs), None
    except Exception as e:
        return None, str(e)

from pydub import AudioSegment

def get_audio_duration(audio_file_path):
    audio = AudioSegment.from_file(audio_file_path)
    return len(audio) / 1000.0  # duration in seconds

def estimate_cost(provider, duration_sec):
    # Real cost logic per provider
    # All costs are per minute, so convert seconds to minutes
    duration_min = duration_sec / 60.0
    if provider == "OpenAI":
        return round(0.006 * duration_min, 4)
    if provider == "Google Gemini":
        return round(0.016 * duration_min, 4)
    if provider == "ElevenLabs":
        return round(0.10 * duration_min, 4)
    if provider == "Sarvam AI":
        return round(0.01 * duration_min, 4)  # Placeholder, update if real pricing is known
    return 0
