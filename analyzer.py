import os
from dotenv import load_dotenv
from google import genai

# Load API Key
load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def analyze_resume(resume_text, job_description):

    prompt = f"""
You are an expert ATS Resume Analyzer.

Compare the following Resume and Job Description.

Resume:
{resume_text}

Job Description:
{job_description}

Return the response in this format:

ATS Score: XX/100

Matching Skills:
- Skill 1
- Skill 2

Missing Skills:
- Skill 1
- Skill 2

Suggestions:
- Suggestion 1
- Suggestion 2

Overall Feedback:
Write a short paragraph.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text