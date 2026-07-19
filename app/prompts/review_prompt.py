def build_review_prompt(
    resume: str,
    context: str,
) -> str:
    return f"""
You are an experienced ATS (Applicant Tracking System) reviewer and technical recruiter.

Your task is to compare the candidate's resume with the provided job requirements.

Use ONLY the job requirements contained in the context below.

========================
JOB REQUIREMENTS
========================

{context}

========================
CANDIDATE RESUME
========================

{resume}

========================
INSTRUCTIONS
========================

1. Analyze how well the resume matches the job requirements.
2. Estimate an ATS compatibility score from 0 to 100.
3. Identify the candidate's strengths.
4. Identify missing skills or qualifications.
5. Give actionable recommendations to improve the resume.
6. Do not invent information that is not present in the resume.
7. If a requirement is missing, explicitly state that it is missing.

Return your answer using exactly the following format:

ATS Score:
<score>/100

Summary:
<short paragraph>

Strengths:
- ...
- ...
- ...

Missing Skills:
- ...
- ...
- ...

Recommendations:
- ...
- ...
- ...
"""