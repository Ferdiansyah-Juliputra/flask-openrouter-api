from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.config.config import (
    CHUNK_SIZE,
    CHUNK_OVERLAP,
)

splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP,
    separators= [
        "\n\n",
        "\n",
        ". ",
        ", ",
        " ",
        "",
    ],
)

def split(text: str):
    return splitter.create_documents([text])