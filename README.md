# Voice-Bot-SDK
Voice-Bot-SDK is a Python SDK designed to process audio inputs, transcribe them using OpenAI's Whisper API, generate responses using GPT-3.5, and synthesize the responses into audio. 
## Setup
- Prerequisites
- Python 3.12
- Virtual environment setup (venv)
- API keys for OpenAI

### Installation 
- clone the repo:
```
git clone https://github.com/yourusername/voice-bot-sdk.git
cd voice-bot-sdk
```
- Create and activate a virtual environment
```
python3.12 -m venv venv
source venv/bin/activate
```
- Install dependencies:
```
pip install -r requirements.txt
```
Replace YOUR_NEW_API_KEY in voice_bot.py with your OpenAI API key.

### Running the SDK

```
python -m voice_bot.voice_bot

```
This command will transcribe the audio file Samplevoice.wav, generate a response using GPT-3.5, synthesize the response using the mock TTS engine, and save the audio response as response.mp3.

### Code overview 
- The SDK uses Python's asyncio library to handle asynchronous tasks, ensuring non-blocking operations for STT, LLM, and TTS functionalities.
- Print statements are used to log key events such as transcription results and generated responses. For a production environment, integrating a logging framework can be considered.

The SDK follows principles of good API design:
- Consistency: Uniform function signatures and class methods.
- Simplicity: Clear and simple interfaces for each component.
- Extensibility: Easily extendable to integrate real TTS engines or other STT services.

### Abstractions 
The SDK employs abstraction to separate concerns:

- OpenAIWhisperSTT: Handles speech-to-text transcription.
- MockTTSEngine: Simulates text-to-speech synthesis.
- OpenAIGPT: Generates responses using GPT-3.5.
- VoiceBotSDK: Orchestrates the interaction between STT, LLM, and TTS components.

### Assumptions and potential issues
- Open AI API doesn't always work as expected so there can be problems with its usage.
- Open AI doesn't have any TTS API so for the purpose of this assignment I have used a mock TTS to showcase the usage of any TTS available online (for example google cloud)
  



