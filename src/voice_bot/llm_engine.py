# src/voice_bot/llm_engine.py
import openai

class OpenAIGPT:
    def __init__(self, api_key, system_prompt="You are a helpful assistant."):
        self.api_key = api_key
        self.system_prompt = system_prompt
        openai.api_key = api_key

    async def generate_response(self, prompt):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=self.system_prompt + "\n\n" + prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
