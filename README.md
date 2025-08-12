# Language Detection API

A FastAPI-based service for spoken language detection from audio files, leveraging multiple state-of-the-art providers (OpenAI, Google Gemini, ElevenLabs, Sarvam AI) for robust and comparative results.

---

## Table of Contents
- [About The Project](#about-the-project)
- [Features](#features)
- [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
- [Usage](#usage)
- [API Reference](#api-reference)
- [Testing](#testing)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)

---

## About The Project

This project provides a unified API to detect the spoken language in an audio file using multiple AI providers. It is designed for benchmarking, research, and production use cases where robust language detection is required.

## Features
- **Multi-provider support:** OpenAI Whisper, Google Gemini, ElevenLabs, Sarvam AI
- **Unified API:** Single endpoint to get results from all providers
- **Cost estimation:** Estimates API cost per provider
- **Extensible:** Easily add new providers
- **Test suite:** Includes tests for API, connectors, and coordinator logic

## Built With
- [FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [Requests](https://docs.python-requests.org/)
- [pydub](https://github.com/jiaaro/pydub)
- [openai](https://github.com/openai/openai-python)
- [google-generativeai](https://github.com/google/generative-ai-python)
- [pytest](https://docs.pytest.org/)

## Getting Started

### Prerequisites
- Python 3.8+
- API keys for each provider you wish to use:
  - `OPENAI_API_KEY`
  - `GEMINI_API_KEY`
  - `ELEVENLABS_API_KEY`
  - `SARVAM_API_KEY`

### Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your_username/language_detection.git
   cd language_detection
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up environment variables:**
   - Create a `.env` file in the project root with the following (fill in your keys):
     ```env
     OPENAI_API_KEY=your_openai_key
     GEMINI_API_KEY=your_gemini_key
     ELEVENLABS_API_KEY=your_elevenlabs_key
     SARVAM_API_KEY=your_sarvam_key
     ```

### Configuration
- Ensure your `.env` file is present and all required API keys are set.
- Audio files should be in a format supported by the providers (e.g., WAV).

## Usage

### Run the API server
```bash
uvicorn api:app --reload
```

### Example API Request
Send a POST request to `/detect/language`:
```json
POST /detect/language
{
  "audio_file_path": "/path/to/audio.wav",
  "ground_truth_language": "en"  // optional, for context
}
```

#### Example Response
```json
{
  "results": [
    {
      "provider": "OpenAI",
      "language": "en",
      "time_taken": 1.23,
      "cost": 0.01,
      "status": "success",
      "error": null
    },
    {
      "provider": "Google Gemini",
      "language": "en",
      "time_taken": 1.45,
      "cost": 0.02,
      "status": "success",
      "error": null
    },
    // ... other providers
  ]
}
```

## API Reference

### `POST /detect/language`
- **Request Body:**
  - `audio_file_path` (str, required): Path to the audio file on the server
  - `ground_truth_language` (str, optional): For context/benchmarking
- **Response:**
  - `results` (list): List of results from each provider
    - `provider`: Provider name
    - `language`: Detected language code
    - `time_taken`: Time taken in seconds
    - `cost`: Estimated cost in USD
    - `status`: `success` or `error`
    - `error`: Error message if any

## Testing

Run all tests with:
```bash
pytest
```

## Roadmap
- [ ] Add support for more providers
- [ ] Dockerize the application
- [ ] Add audio file upload endpoint
- [ ] Improve error handling and logging
- [ ] Add more detailed benchmarking tools

## Contributing
Contributions are welcome! Please open issues or pull requests for improvements, bug fixes, or new features.

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request

## License
Distributed under the MIT License. See `LICENSE` for more information.

## Contact
Project Maintainer: [Parthib Mukherjee](mailto:parthibmukherjee@gmail.com)

## Acknowledgments
- [othneildrew/Best-README-Template](https://github.com/othneildrew/Best-README-Template)
- [FastAPI](https://fastapi.tiangolo.com/)
- [OpenAI](https://openai.com/)
- [Google Gemini](https://ai.google.dev/)
- [ElevenLabs](https://elevenlabs.io/)
- [Sarvam AI](https://sarvam.ai/)
