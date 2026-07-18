from langchain import PyPDFLoader, WebBaseLoader
import bs4

def load_from_url(url):
    loader = WebBaseLoader(
        web_path=url,
        bs_kwargs=dict(parse_only=bs4.SoupStrainer("p"))
    )
    return loader.load()

def load_from_pdf(file_path):
    loader = PyPDFLoader(file_path)
    return loader.load()