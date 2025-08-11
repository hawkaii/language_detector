from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from coordinator import run_all_providers
import os

app = FastAPI()

class DetectRequest(BaseModel):
    audio_file_path: str
    ground_truth_language: str = None  # For context only

@app.post("/detect/language")
def detect_language(request: DetectRequest):
    # Validate audio file path
    if not os.path.isfile(request.audio_file_path):
        raise HTTPException(status_code=400, detail="Audio file not found.")
    results = run_all_providers(request.audio_file_path)
    return {"results": results}
