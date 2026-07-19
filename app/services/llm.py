from app.config.config import LLM_PROVIDER
from app.services.providers import ollama, openrouter

PROVIDERS={
    "ollama": ollama,
    "openrouter": openrouter
}

def generate_response(prompt:str) -> str:
    provider = PROVIDERS.get(LLM_PROVIDER)

    if provider is None:
        raise ValueError(f"Unsupported provider: {LLM_PROVIDER}")
    
    return provider.generate(prompt)