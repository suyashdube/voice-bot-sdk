# src/voice_bot/tts_engine.py
import aiohttp

class MockTTSEngine:
    def __init__(self, api_key):
        self.api_key = api_key

    async def synthesize(self, text):
        # Simulate a TTS engine call
        return f"Audio data for: {text}"
