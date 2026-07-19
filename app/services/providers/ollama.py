from langchain_ollama import OllamaLLM
from app.config.config import OLLAMA_MODEL

llm = OllamaLLM(
    model=OLLAMA_MODEL,
)

def generate(prompt:str)->str:
    return llm.invoke (prompt)