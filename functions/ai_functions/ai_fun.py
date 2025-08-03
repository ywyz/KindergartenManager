from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("DEEPSEEK_KEY"), base_url=os.getenv("DEEPSEEK_URL", "https://api.deepseek.com/v1"))

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    stream=False
)

print(response.choices[0].message.content)