#Example Code

import openai

openai.api_base = "https://openrouter.ai/api/v1"
openai.api_key = "your_api_key"

response = openai.ChatCompletion.create(
    model="openrouter/openai/gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain Agentic AI."}
    ]
)

print(response.choices[0].message["content"])
