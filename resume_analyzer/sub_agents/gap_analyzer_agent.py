from google.adk.agents import Agent
from google.adk.tools import google_search
from ..tools.resume_tools import calculate_keyword_match_score

gap_analyzer_agent = Agent(
    name="gap_analyzer_agent",
    model="gemini-2.0-flash-lite",
    description="Compares resume vs job description and identifies gaps.",
    instruction="""
You are a Career Coach and Resume Gap Analyst.

Your job:
1. Receive resume text and job description text.
2. Use calculate_keyword_match_score with both texts to get a match score.
3. Analyze: missing critical skills, undemonstrated experience, strengths, weaknesses.
4. Use google_search if needed to clarify technical terms.
5. Provide: match score summary, top 5 strengths, top 5 gaps, prioritized 
   keyword recommendations with WHERE to add them in the resume.
""",
    tools=[calculate_keyword_match_score, google_search],
)