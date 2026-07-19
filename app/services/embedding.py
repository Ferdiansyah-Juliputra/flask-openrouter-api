from pathlib import Path
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.logger.logger import logger
from app.config.config import (
    EMBEDDING_MODEL,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
)

EMBEDDINGS = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

def split_documents(docs: list[Document]) -> list[Document]:
    logger.info(f"Splitting documents into chunks of size {CHUNK_SIZE} with overlap {CHUNK_OVERLAP}")
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    )
    logger.info(f"Splitting {len(docs)} documents into chunks")
    return splitter.split_documents(docs)
