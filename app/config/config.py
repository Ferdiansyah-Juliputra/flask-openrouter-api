import os
from dotenv import load_dotenv

load_dotenv()

# ======== LLM Provider =========
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "ollama")

# ========= OpenRouter =========
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_MODEL = os.getenv("OPENROUTER_MODEL")
OPENROUTER_BASE_URL = os.getenv("OPENROUTER_BASE_URL")

# ========= Embedding =========
EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "sentence-transformers/paraphrase-MiniLM-L6-v2",
)

# ========= Chroma =========
VECTOR_DB_PATH = os.getenv("VECTOR_DB_PATH", "vector_db")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "documents")

# ========= Text Splitter =========
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 1000))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 100))

# ======== Retriever =========
RETRIEVER_K = int(os.getenv("RETRIEVER_K", 5))

# ======== Ollama =========
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen3:4b")