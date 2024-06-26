import os
import aiohttp
import asyncio
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class VoiceBotSDK:
    def __init__(self):
        self.stt_engine = None
        self.tts_engine = None
        self.llm_engine = None

    def setup(self, stt_config, tts_config, llm_config):
        if stt_config['name'] == 'openai':
            self.stt_engine = OpenAIWhisperSTT(stt_config['api_key'])
        if tts_config['name'] == 'mock':
            self.tts_engine = MockTTSEngine()
        if llm_config['name'] == 'openai':
            self.llm_engine = OpenAIGPT(llm_config['api_key'], llm_config['system_prompt'])

    async def transcribe_file(self, file_path):
        with open(file_path, 'rb') as audio_file:
            transcript = await self.stt_engine.transcribe(audio_file)
            print(f"Transcript: {transcript}")
            return transcript

class OpenAIWhisperSTT:
    # def __init__(self, api_key):
    #     self.api_key = api_key

    async def transcribe(self, audio_file):
        async with aiohttp.ClientSession() as session:
            response = await session.post(
                'https://api.openai.com/v1/audio/transcriptions',
                headers={'Authorization': f'Bearer {self.api_key}'},
                data={'file': audio_file, 'model': 'whisper-1'}
            )
            if response.status != 200:
                raise Exception(f"Failed to transcribe: {response.status}, {await response.text()}")
            result = await response.json()
            return result['text']

class MockTTSEngine:
    async def synthesize(self, text):
        return "This is a mock synthesis of: " + text

if __name__ == "__main__":
    sdk = VoiceBotSDK()
    sdk.setup(
        stt_config={'name': 'openai', 'api_key': os.getenv('OPENAI_API_KEY')},
        tts_config={'name': 'mock'},
        llm_config={'name': 'openai', 'api_key': os.getenv('OPENAI_API_KEY'), 'system_prompt': 'Your system prompt here'}
    )

    audio_file_path = '/path/to/Samplevoice.wav'
    asyncio.run(sdk.transcribe_file(audio_file_path))
