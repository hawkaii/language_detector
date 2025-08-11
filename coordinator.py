from connectors.openai import detect_language as openai_detect
from connectors.gemini import detect_language as gemini_detect
from connectors.sarvam import detect_language as sarvam_detect
from connectors.elevenlabs import detect_language as elevenlabs_detect


def run_all_providers(audio_file_path):
    results = []
    for provider_func in [openai_detect, gemini_detect, sarvam_detect, elevenlabs_detect]:
        result = provider_func(audio_file_path)
        results.append(result)
    return results
