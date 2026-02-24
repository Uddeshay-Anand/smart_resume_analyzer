from google.adk.agents import Agent
from google.adk.tools import google_search

jd_analyzer_agent = Agent(
    name="jd_analyzer_agent",
    model="gemini-2.0-flash-lite",
    description="Analyzes job descriptions and extracts required skills and keywords.",
    instruction="""
You are a Job Description Analysis Expert.

Your job:
1. Read the job description provided.
2. Extract: Job Title, Required Hard Skills, Preferred Skills, Soft Skills,
   Key Responsibilities, Experience Level, Education, ATS Keywords.
3. If only a job title is given (no full JD), use google_search to find 
   typical requirements for that role.
4. Return a structured breakdown.
""",
    tools=[google_search],
)