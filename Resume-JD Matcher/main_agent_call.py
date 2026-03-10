import os 
from dotenv import load_dotenv
from pathlib import Path


current_dir = Path(__file__).resolve().parent

# Go up one level to find the .env file in the root directory
env_path = current_dir.parent / '.env'

# This function will load all the variables from the .env file and will 
# make them available in the os.environ dictionary (env variables)
#load_dotenv() 
load_dotenv(dotenv_path=env_path)



dummy_resume = """
Mehar Singh Bawa
bawamehar@gmail.com +1 9705661937 linkedin.com/in/bawamehar/ github.com/bawamehar
PROFILE
Data Specialist with a proven track record of optimizing business processes and reducing operational risk. Brings
5 years of industry experience in diagnostics and process automation, now applied to Predictive Modeling and
Data Visualization. Expert in bridging the gap between technical metrics and business goals, seeking to leverage
advanced analytics skills to solve complex data challenges.
EDUCATION
Masters in Computer Information Systems
Colorado State University
01/2025 – Present
•Coursework: Business Intelligence, Applied Data Mining and Analytics, Enterprise Resource Planning.
•Graduate Assistant for Analytics and AI in Business.
•Member of Dean’s List for Spring 2025, Fall 2026.
B-Tech in Computer Science and Engineering
SRM Institute of Science and Technology
05/2019
MACHINE LEARNING & DATA PROJECTS
Airline Passenger Satisfaction 12/2025
•Predicted airline passenger satisfaction using machine learning.Includes data preprocessing, visualization,
feature scaling, multiple models (Logistic Regression,Random Forest,Adaboost, etc), cross-validation, and
feature importance analysis.
Diabetes Prediction Project
•Architected a ML application featuring a Streamlit UI and FastAPI backend to automate real-time diabetes risk
assessment and store patient data in PostgreSQL.
•Developed a training pipeline that evaluates multiple classifiers models, exports the best model via Joblib, and
uses MLOps for production orchestration and model versioning.
SAP ERP Simulation Game, Colorado State University
CIS601 Enterprise Computing & SystemsIntegration
05/2025
•Managed a Muesli Manufacturing Company using SAP ERP, engaging in complex business processes from raw
material acquisition to product sales. Leveraged Microsoft Power BI to analyze and interpret data, making datadriven decisions that led to a competitive advantage over rivals and resulted in winning the game.
Electric Vehicle Analysis, Colorado State University
CIS570 BusinessIntelligence
05/2025
•Conducted data analysis on EV adoption, sales trends, charging efficiency, economic benefits and impact using
Power BI, creating interactive dashboards to highlight patterns and support data-driven decision-making.
PROFESSIONAL EXPERIENCE
Consultant
Capgemini
02/2020 – 01/2025 | Pune,IN
•Developed multiple automated processes to minimize the manual tasks and enhanced the service delivery.
•Maintained high-availability production environments on AWS, utilizing Dynatrace for root-cause analysis of
system outages.
•Translated vague client requirements into measurable KPIs, using data analysis to prioritize features and
optimize delivery.
•Analysed and visualized historical failure patterns using FMEA methodology, interpreting key data trends to
optimize business processes and achieve a 70% reduction in problems.
SKILLS & CERTIFICATIONS
Skills: Python (pandas, scikit-learn), AWS, Power BI, Snowflake, R, Tableau, Knime, SQL, Dynatrace, LangChain
Certification: AWS Certified Developer- Associate, Certified SAFe 6 Scrum Master
"""

dummy_jd = """
Job Description

**This is a fully on-site role. Hybrid/remote work is not available at this time**

**We are unable to sponsor or take over sponsorship of an employment Visa at this time**




Are you early in your data science career and eager to work on real, production‑impacting models? RIVO is excited to find our next Junior Data Scientist to join our Data Team and help build the data pipelines, features, and model experiments that power our decision‑making tools within our Risk & Underwriting teams.


This is a great role for someone who is eager to learn and be mentored by senior team members, loves hands‑on data work, and has a knack for solving analytical problems. If you're excited about solving meaningful problems with data — and growing your skills along the way — we’d love to hear from you!




What You’ll Do:


Build and maintain feature pipelines that support risk and underwriting models.
Use Python and SQL to explore, transform, and prepare datasets for modeling.
Assist with training, validating, and monitoring predictive models — including probability‑of‑default and other underwriting scores.
Support A/B testing and champion/challenger experiments to evaluate new features and model improvements.
Look for opportunities to apply AI tools to streamline workflows and enhance analysis
Identify and troubleshoot data quality issues such as anomalies, schema drift, or inconsistent signals.
Collaborate with Underwriting, Data Engineering, and Analytics partners to translate business questions into analytical solutions.
Contribute to improving our model infrastructure, pipelines, and analytical workflows.
Why You’ll Love Working Here:


Collaborative team culture with strong mentorship to grow your data science skills
Work directly on high‑impact models used across the business
Exposure to real‑world ML workflows in production
Opportunities to grow into more advanced modeling, experimentation, or analytics engineering paths

Qualifications

What You Bring:


Bachelor’s degree in Data Science, Computer Science, Statistics, Mathematics, Economics, Engineering, or a related quantitative field required.
1–3 years of experience (including internships) in data science, analytics, or a similar applied role required.
A strong foundation in Python and SQL for data manipulation and modeling.
Solid understanding of core machine learning concepts (classification, validation methods, evaluation metrics).
Familiarity with EDA and hands‑on experience working with structured (and ideally some unstructured) datasets.
A growth mindset — you’re eager to learn, ask thoughtful questions, and proactively seek clarity when needed.
A natural sense of curiosity and genuine passion for data science and machine learning.
Willingness to upskill independently, explore new tools or techniques, and bring fresh ideas to the team.
A proactive interest in using AI tools to learn faster, work smarter, and boost team impact.
Strong attention to detail and an appreciation for clean, well‑structured, reliable data.
Comfortable communicating your findings clearly to your manager and project partners.
Experience with Git/GitHub is a plus (or excitement to learn it quickly).

"""

# Agent Imports

# from agents.parser_agent_1 import get_parsed_data
# from agents.matcher_agent_2 import get_match_results


# #Agent 1

# # Parse Resume
# print("Parsing Resume...")
# resume_json = get_parsed_data("Resume", dummy_resume)

# # Parse JD
# print("Parsing JD...")
# jd_json = get_parsed_data("Job Description", dummy_jd)

# print("--- RESUME JSON ---")
# print(resume_json.model_dump_json(indent=2))

# print("\n--- JD JSON ---")
# print(jd_json.model_dump_json(indent=2))


# #Agent 2
# # Run Agent 2
# match_output = get_match_results(resume_json, jd_json)

# # Print the report
# print_basic_report(match_output)


from graph import app
#from core.utils import print_basic_report, print_coach_report, print_ats_report
from core.utils import format_basic_report, format_ats_report, format_coach_report

def run_pipeline():
    """Orchestrates the agentic workflow via LangGraph."""
    
    if os.environ.get("OPENAI_API_KEY"):
        print("API KEY Variable exists")
    else:
        raise ValueError("OPENAI_API_KEY not found")

    # The inputs  Graph needs to start
    initial_state = {
        "raw_resume": dummy_resume, 
        "raw_jd": dummy_jd
    }

    print("Starting LangGraph Workflow...")
    
    # Trigger the compiled Graph
    # This automatically runs Nodes in order
    final_state = app.invoke(initial_state)

    # Extract and print the results from the shared State
    if "match_results" in final_state:
        #print_basic_report(final_state["match_results"])
        print(format_basic_report(final_state["match_results"]))
    else:
        print("Error: Pipeline completed but match_results are missing.")

    
    # Print ATS Results (Agent 3)
    if "ats_results" in final_state:
        #print_ats_report(final_state["ats_results"])
        print("\n" + "="*20 + "\n")
        print(format_ats_report(final_state["ats_results"]))
    
    
    # Print Coach Results (Agent 4)
    if "coach_results" in final_state and final_state["coach_results"]:
        #print_coach_report(final_state["coach_results"])
        print("\n" + "="*20 + "\n")
        print(format_coach_report(final_state["coach_results"]))


if __name__ == "__main__":
    run_pipeline()