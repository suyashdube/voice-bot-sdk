# src/voice_bot/whisper_stt.py
import openai
import aiohttp
import certifi
import ssl

class OpenAIWhisperSTT:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = api_key

    async def transcribe(self, audio_data):
        headers = {
            'Authorization': f'Bearer {self.api_key}',
        }
        ssl_context = ssl.create_default_context(cafile=certifi.where())
        async with aiohttp.ClientSession() as session:
            async with session.post(
                'https://api.openai.com/v1/audio/transcriptions',
                headers=headers,
                data={'file': audio_data, 'model': 'whisper-1'},
                ssl=ssl_context
            ) as response:
                if response.status != 200:
                    raise Exception(f"Failed to transcribe: {response.status}, {await response.text()}")
                response_json = await response.json()
                return response_json['text']

