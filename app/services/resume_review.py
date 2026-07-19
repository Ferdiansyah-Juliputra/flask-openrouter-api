from app.prompts.review_prompt import build_review_prompt
from app.services.llm import generate_response


def review_resume(
    resume: str,
    requirement: str,
) -> str:

    prompt = build_review_prompt(
        resume=resume,
        requirement=requirement,
    )

    return generate_response(prompt)