from andromeda.config import ModelConfig

MODEL_CONFIG = ModelConfig(
    name="llama3.1:8b",
    provider="ollama",
    other_args={
        "base_url": "http://localhost:11434",
        "temperature": 0
    }
)