import os
from dotenv import load_dotenv

load_dotenv()

# ======== LLM Provider =========
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "openrouter")

# ========= OpenRouter =========
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_MODEL = os.getenv("OPENROUTER_MODEL")
OPENROUTER_BASE_URL = os.getenv("OPENROUTER_BASE_URL")

# ========= Embedding =========
EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "sentence-transformers/paraphrase-MiniLM-L6-v2",
)

UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "app/storage/uploads")