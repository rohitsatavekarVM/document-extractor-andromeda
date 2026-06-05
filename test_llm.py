# test_llm.py

from litellm import completion

response = completion(
    model="ollama/qwen3:8b",
    api_base="http://localhost:11434",
    messages=[
        {
            "role": "user",
            "content": "Respond with hello"
        }
    ]
)

print(response.choices[0].message.content)