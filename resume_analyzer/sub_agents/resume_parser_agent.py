from google.adk.agents import Agent
from ..tools.resume_tools import extract_pdf_text, extract_text_from_file

resume_parser_agent = Agent(
    name="resume_parser_agent",
    model="gemini-2.0-flash-lite",
    description="Extracts and structures text from resume files (PDF or TXT).",
    instruction="""
You are a Resume Parsing Specialist.

Your job:
1. Use the appropriate tool to extract text from the provided resume file path.
   - Use extract_pdf_text for .pdf files.
   - Use extract_text_from_file for .txt files.
2. Structure the content into: Candidate Name, Contact Info, Summary, 
   Work Experience, Education, Skills, Certifications.
3. Return a clean structured summary.
""",
    tools=[extract_pdf_text, extract_text_from_file],
)