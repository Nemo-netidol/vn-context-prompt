from dotenv import load_dotenv
import os
from openai import OpenAI
import json

load_dotenv()

API_KEY = os.getenv("API_KEY")


systemPrompt = open("prompt/system_prompt.txt").read()


client = OpenAI(api_key=API_KEY)

def generate_context(user_prompt: str):

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
            "role": "system",
            "content": systemPrompt
        }, {
            "role": "user",
            "content": user_prompt
        }
        ]   
    )

    response = completion.choices[0].message.content
    return response