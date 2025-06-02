import os
from litellm import completion


os.environ["OPENAI_API_KEY"] = ""
os.environ["ANTHROPIC_API_KEY"] = ""


def use_openai():
    response = completion(
        model="openai/gpt-4o",
        messages=[
            {
                "role": "user",
                "content": "Hello, how are you?"
            }
        ]
    )
    print(response)

def use_claude():
    response = completion(
        model="claude/claude-3-sonnet",
        messages=[
            {
                "role": "user",
                "content": "Hello, how are you?"
            }
        ]
    )
    print(response)


def use_claude_opus():
    response = completion(
        model="claude/claude-3-opus",
        messages=[
            {
                "role": "user",
                "content": "Hello, how are you?"
            }
        ]
    )
    print(response)



