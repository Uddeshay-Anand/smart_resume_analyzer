# Smart Resume Analyzer 🎯

A multi-agent AI system built with Google ADK that analyzes your resume against
a job description and provides keyword improvement suggestions.

## Architecture

- **Root Agent** (`smart_resume_analyzer`): Orchestrates the full pipeline
- **Resume Parser Agent**: Extracts and structures resume content from PDF/TXT
- **JD Analyzer Agent**: Analyzes job description using Google Search when needed
- **Gap Analyzer Agent**: Compares resume vs JD, calculates match score
- **Report Generator Agent**: Creates a formatted Markdown report

## Setup

1. **Clone the repo**
```bash
   git clone <your-repo-url>
   cd smart_resume_analyzer
```

2. **Create virtual environment**
```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

3. **Install dependencies**
```bash
   pip install -r requirements.txt
```

4. **Configure API key**
```bash
   cp .env.example .env
   # Edit .env and add your GOOGLE_API_KEY
```

## Running the Agent

Always run from the root project directory (parent of `resume_analyzer/`):
```bash
# Web UI (recommended)
adk web

# CLI mode
adk run resume_analyzer
```

## Usage

1. Start the agent
2. Provide your resume (file path or paste text)
3. Provide the job description (paste text or job title)
4. The system analyzes and generates `resume_analysis_report.md`

## Custom Tools

- `extract_pdf_text` — Reads PDF resume files
- `extract_text_from_file` — Reads TXT resume files  
- `calculate_keyword_match_score` — Computes ATS keyword match %
- `generate_markdown_report` — Saves formatted analysis report

## Built-in Tools

- `google_search` — Used to research job market requirements
```

---

## PHASE 4: Running & Testing (10 minutes)

### Step 1 — Verify your folder structure looks like this:
```
smart_resume_analyzer/           ← you are here when running commands
├── .env
├── .gitignore
├── requirements.txt
├── README.md
├── problem_statement.md
└── resume_analyzer/
    ├── __init__.py
    ├── agent.py
    ├── sub_agents/
    │   ├── __init__.py
    │   ├── resume_parser_agent.py
    │   ├── jd_analyzer_agent.py
    │   ├── gap_analyzer_agent.py
    │   └── report_generator_agent.py
    └── tools/
        ├── __init__.py
        └── resume_tools.py