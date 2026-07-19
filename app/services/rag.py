from app.config.config import RETRIEVER_K
from app.prompts.resume_review import build_prompt
from app.services.llm import generate_response
from app.services.vector_store import get_retriever


def review_resume(
    resume: str,
    requirement: str,
) -> str:

    retriever = get_retriever(k=RETRIEVER_K)

    docs = retriever.invoke(requirement)

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    prompt = build_prompt(
        resume=resume,
        context=context,
    )

    return generate_response(prompt)