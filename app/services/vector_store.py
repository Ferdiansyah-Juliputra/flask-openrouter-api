from pathlib import Path
from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from app.logger.logger import logger
from app.config.config import (
    VECTOR_DB_PATH,
    COLLECTION_NAME,
    EMBEDDING_MODEL,
)
EMBEDDINGS = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

def create_vector_store(
    documents: list[Document],
) -> Chroma:
    logger.info(f"Creating vector store at {Path(VECTOR_DB_PATH).resolve()}")
    return Chroma.from_documents(
        documents=documents,
        embedding=EMBEDDINGS,
        persist_directory=VECTOR_DB_PATH,
        collection_name=COLLECTION_NAME,
    )

def load_vector_store(
) -> Chroma:
    return Chroma(
        persist_directory=VECTOR_DB_PATH,
        embedding_function=EMBEDDINGS,
        collection_name=COLLECTION_NAME,
    )