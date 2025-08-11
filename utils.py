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

def estimate_cost(provider, duration_sec):
    # Placeholder: real cost logic should be implemented per provider
    if provider in ("OpenAI", "Google Gemini"):
        return 0.01 * duration_sec  # Example: $0.01 per second
    return 0
