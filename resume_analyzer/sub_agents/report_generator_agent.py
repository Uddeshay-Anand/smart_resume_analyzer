from google.adk.agents import Agent
from ..tools.resume_tools import generate_markdown_report

report_generator_agent = Agent(
    name="report_generator_agent",
    model="gemini-2.0-flash-lite",
    description="Compiles all analysis into a formatted Markdown report.",
    instruction="""
You are a Technical Report Writer.

Your job:
1. Receive all analysis results (candidate name, job title, match score, 
   matched keywords, missing keywords, strengths, weaknesses, recommendations).
2. Call generate_markdown_report with ALL fields filled in clearly.
3. After saving, tell the user the file was saved and summarize:
   - Match score
   - Top 3 missing keywords
   - Most important recommendation
""",
    tools=[generate_markdown_report],
)