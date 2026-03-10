import streamlit as st
from dotenv import load_dotenv
from pathlib import Path



# Get the path to the directory where agent_call.py is located
current_dir = Path(__file__).resolve().parent

# Go up one level to find the .env file in the root directory
env_path = current_dir.parent / '.env'

# This function will load all the variables from the .env file and will 
# make them available in the os.environ dictionary (env variables)
#load_dotenv() 
load_dotenv(dotenv_path=env_path)

st.set_page_config(page_title="Resume-JD Matcher AI", layout="wide")

st.title("AI Resume-JD Matcher & Career Coach")
st.subheader("Optimizing your path to the next role and beyond.")

from graph import app 
from core.utils import extract_text_from_file, format_basic_report, format_ats_report, format_coach_report, format_action_plan

# --- Sidebar / Inputs ---
with st.sidebar:
    st.header("Upload Documents")
    uploaded_resume = st.file_uploader("Upload Resume (PDF/DOCX)", type=["pdf", "docx"])
    jd_text = st.text_area("Paste Job Description Here", height=300)

# --- Execution ---
if st.button("Compare", type="primary"):
    if uploaded_resume and jd_text:
        with st.spinner("Agents are analyzing your data..."):
            # 1. Extract Resume Text
            resume_text = extract_text_from_file(uploaded_resume)
            
            # 2. Run LangGraph
            inputs = {"raw_resume": resume_text, "raw_jd": jd_text}
            final_state = app.invoke(inputs)
            
            # 3. Display Results in Tabs
            tab1, tab2, tab3, tab4 = st.tabs(["Summary", "Match Score", "ATS Audit", "Career Coach"])
            
            with tab2:
                st.header("Match Analysis")
                st.markdown(format_basic_report(final_state["match_results"]))
                
            with tab3:
                st.markdown(format_ats_report(final_state["ats_results"]))
                
            with tab4:
                st.markdown(format_coach_report(final_state["coach_results"]))

            with tab1:
                target = final_state["jd_obj"].job_title
                st.header(f"⚡ 1-Minute Action Plan for {target}")
                st.markdown(format_action_plan(final_state))
                
    else:
        st.warning("Please upload a resume and paste a JD first!")