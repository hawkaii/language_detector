# Implementation Plan for Language Detective Service

## 1. Project Structure
- **connectors/**: Individual provider connectors (OpenAI, Google Gemini, Sarvam AI, ElevenLabs)
- **coordinator.py**: Orchestrates calls to all connectors, aggregates results
- **api.py**: FastAPI app exposing the /detect/language endpoint
- **utils.py**: Shared utilities (timing, error handling, cost estimation)
- **tests/**: Unit and integration tests

## 2. Provider Connectors
- Implement 4 connector functions (one per provider):
  - Each accepts an audio file path
  - Returns a language code (e.g., 'en', 'hi', 'ta')
  - Handles errors gracefully (returns error info, does not crash)
  - At least 2 connectors (OpenAI, Google Gemini) use real API calls
  - The other 2 (Sarvam AI, ElevenLabs) return fixed mock responses

## 3. Coordinator Function
- Calls all 4 connectors for a given audio file
- For each provider, records:
  - Provider name
  - Detected language
  - Time taken (seconds)
  - Estimated cost (tokens, dollar usage)
  - Status (success, failure, error)
  - Error message (if any)
- Aggregates results into a list

## 4. FastAPI Endpoint
- POST /detect/language
- Request: JSON with `audio_file_path` and `ground_truth_language`
- Response: JSON list of results from all 4 providers (with all details above)
- Robust error handling for invalid input, missing files, etc.

## 5. Error Handling & Reporting
- All connectors and coordinator must handle API/network errors robustly
- All errors are reported in the response (not as exceptions)

## 6. Bonus Objectives
- Optimize for Indian language accuracy (test with relevant samples)
- Minimize detection time (parallelize connector calls if possible)

## 7. Testing
- Unit tests for each connector (mocking APIs as needed)
- Integration tests for coordinator and API endpoint

## 8. Tools & Dependencies
- Python 3.10+
- FastAPI
- UV (Astral) for package management
- Requests/HTTPX for API calls
- Pytest for testing

---

This plan ensures modularity, robust error handling, and clear separation of concerns, matching all requirements from the assignment.
