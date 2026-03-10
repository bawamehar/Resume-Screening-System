# AI Resume-JD Matcher & Career Coach

An **Agentic AI** system built to match candidate profiles with complex Job Descriptions (JD). Leveraging **LangGraph** for stateful orchestration, **OpenAI** for high-reasoning extraction, and **Streamlit** for real-time visualization, this tool automates technical gap analysis, ATS compatibility auditing. The system is integrated with **LangSmith** for full-trace observability and performance monitoring, ensuring every agentic decision is transparent and optimized for suggested resume reconstruction.

## Key Features

- **Multi-Agent Orchestration**: Powered by LangGraph to manage state across four specialized AI agents.
- **Precision Extraction**: Uses Pydantic-enforced schemas to parse complex Resume.
- **ATS Intelligence**: Heuristic-based scoring for readability and keyword density.
- **Actionable Coaching**: Suggest important changes in resume and tailored interview questions.
- **Executive Summary**: A "1-Minute Action Plan" for rapid application optimization.

## System Architecture

The project follows a modular pipeline where each agent specializes in a specific domain of the recruitment lifecycle.

1. **Parser Agent**: Extracts contact info, skills, and work history.
2. **Matcher Agent**: Evaluates technical alignment and identifies skill gaps.
3. **ATS Specialist**: Audits formatting and keyword searchability.
4. **Career Coach**: Synthesizes findings into a strategic preparation guide.

## Tech Stack

- Orchestration: LangChain & LangGraph

- UI Framework: Streamlit

- LLM: OpenAI GPT-5-mini

- Validation: Pydantic

- Document Processing: PdfPlumber, Python-Docx

- Performance Monitoring: LangSmith

## Getting Started

1. **Installation:** 
Clone the repository and install the required dependencies:
- git clone https://github.com/bawamehar/Resume-Screening-System.git
- pip install -r requirements.txt

2. **Environment Configuration:** 
Create a .env file in the root directory and add your credentials:
- OPENAI_API_KEY=your_openai_api_key_here

3. **Execution:** 
Launch the Streamlit dashboard:
- cd Resume-JD Matcher
- streamlit run app.py

## Project Structure

```text
├── agents/           # Specialized Agent logic (Parser, Matcher, ATS, Coach)
├── core/             # Shared Pydantic models, prompts, and utilities
├── app.py            # Streamlit UI Entry Point
├── graph.py          # LangGraph Workflow Definition
├── main_agent_call.py # CLI Testing Sandbox
└── requirements.txt  # Dependencies
```
**UI**
![Dashboard Preview](dashboard.png)

**Architecture Diagram**
![Architecture Diagram](Architecture_Diagram.png)


![Requirements File](requirements.txt)

**Developed by Mehar Singh Bawa**