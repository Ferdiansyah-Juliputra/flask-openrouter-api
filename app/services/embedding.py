from pathlib import Path
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.logger.logger import logger
from app.config.config import (
    VECTOR_DB_PATH,
    COLLECTION_NAME,
    EMBEDDING_MODEL,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
)

EMBEDDINGS = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

def split_documents(docs: list[Document]) -> list[Document]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    )
    return splitter.split_documents(docs)

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