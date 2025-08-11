import os
from connectors.openai import detect_language as openai_detect
from connectors.gemini import detect_language as gemini_detect
from connectors.sarvam import detect_language as sarvam_detect
from connectors.elevenlabs import detect_language as elevenlabs_detect

# Use a dummy file path for mock tests
DUMMY_AUDIO = __file__  # This file exists, so path is valid

def test_openai_connector():
    result = openai_detect(DUMMY_AUDIO)
    assert 'provider' in result and result['provider'] == 'OpenAI'
    assert 'language' in result
    assert 'status' in result

def test_gemini_connector():
    result = gemini_detect(DUMMY_AUDIO)
    assert 'provider' in result and result['provider'] == 'Google Gemini'
    assert 'language' in result
    assert 'status' in result

def test_sarvam_connector():
    result = sarvam_detect(DUMMY_AUDIO)
    assert 'provider' in result and result['provider'] == 'Sarvam AI'
    assert 'language' in result
    assert 'status' in result

def test_elevenlabs_connector():
    result = elevenlabs_detect(DUMMY_AUDIO)
    assert 'provider' in result and result['provider'] == 'ElevenLabs'
    assert 'language' in result
    assert 'status' in result
