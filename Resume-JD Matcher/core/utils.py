import pdfplumber
from docx import Document
import io


def extract_text_from_file(uploaded_file):
    file_type = uploaded_file.name.split('.')[-1].lower()
    
    if file_type == 'pdf':
        with pdfplumber.open(uploaded_file) as pdf:
            text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
        return text
        
    elif file_type == 'docx':
        doc = Document(uploaded_file)
        return "\n".join([para.text for para in doc.paragraphs])
        
    else:
        return uploaded_file.getvalue().decode("utf-8")



# utils.py needs to import blueprint (MatchResults) so it knows exactly what fields it is allowed to print
from core.models import MatchResults, ATSResults, CoachResults


def format_basic_report(results: MatchResults):
    report = [f"## Match Score: {results.match_score}/100"]
    
    report.append("\n### Evaluation Logic")
    report.append(f"- **Experience:** {results.experience_reasoning}")
    report.append(f"- **Skills:** {results.skill_reasoning}")
    report.append(f"- **Projects:** {results.project_reasoning}")
    report.append(f"- **Education:** {results.education_reasoning}")
    
    report.append("\n### Missing Skills & Gaps")
    if results.missing_skills:
        for s in results.missing_skills:
            status = "**DEALBREAKER**" if s.is_dealbreaker else "Nice-to-have"
            report.append(f"- {s.name} (Priority {s.priority}): {status}")
    else:
        report.append("- No major skill gaps identified!")
        
    report.append(f"\n### Final Audit Summary\n{results.score_justification}")
    return "\n".join(report)


def format_ats_report(results: ATSResults):
    report = [f"## ATS Readability: {results.ats_score}/100", f"**Verdict:** {results.overall_verdict}\n"]
    
    report.append("### Formatting & Structure Warnings")
    if results.formatting_warnings:
        for warn in results.formatting_warnings:
            report.append(f"- **[{warn.issue_type}]**: {warn.description}")
            report.append(f"  *Fix: {warn.fix}*")
    else:
        report.append("- No major formatting risks detected.")
        
    report.append("\n### Keyword Analysis")
    found = ", ".join(results.found_keywords) if results.found_keywords else "None"
    report.append(f"- **Found:** {found}")
    
    missing = ", ".join(results.missing_keywords) if results.missing_keywords else "None (All keywords present!)"
    report.append(f"- **Missing:** {missing}")
    
    return "\n".join(report)


def format_coach_report(results: CoachResults):
    report = ["## Job Application Strategy Guide"]
    
    report.append("\n### Resume Enhancements")
    for i, bullet in enumerate(results.top_3_bullets, 1):
        report.append(f"#### Suggestion {i}")
        report.append(f"- **Context:** {bullet.original_context}")
        report.append(f"- **Modified:** {bullet.suggested_bullet}")
        report.append(f"- **Why:** {bullet.reasoning}\n")

    report.append("### ATS Optimization Quick-Fixes")
    if results.ats_strategy_points:
        for point in results.ats_strategy_points:
            report.append(f"- {point}")
    else:
        report.append("- No specific ATS changes required.")

    report.append("\n### Tailored Interview Preparation")
    for i, qa in enumerate(results.interview_q_and_a, 1):
        report.append(f"**Q{i}: {qa.question}**")
        report.append(f"- *Intent:* {qa.intent}")
        report.append(f"- *Strategy:* {qa.strategy}\n")

    report.append(f"\n---\n**Final Note:** {results.final_encouragement}")
    return "\n".join(report)


def format_action_plan(state):
    match = state.get("match_results")
    ats = state.get("ats_results")
    coach = state.get("coach_results")
    
    report = []

    report.append(f"## Quick Assessment")
    report.append(f"**Match Score:** {match.match_score}/100 | **ATS Score:** {ats.ats_score}/100\n")

    report.append("### Top Missing Skills")
    if match.missing_skills:
        gaps = [f"{s.name}" for s in match.missing_skills[:4]]
        report.append(", ".join(gaps))
    
    # if ats:
    #     report.append(f"\n### ATS Health Check")
    #     report.append(f"**Verdict:** {ats.overall_verdict}\n")

    report.append("\n### Key Resume Edits")
    if coach and coach.top_3_bullets:
        for i, bullet in enumerate(coach.top_3_bullets, 1):
            report.append(f"{i}. **Add/Edit:** {bullet.suggested_bullet}")

    report.append("\n### Interview Focus")
    if coach and coach.interview_q_and_a:
        for i, qa in enumerate(coach.interview_q_and_a, 1):
            report.append(f"{i}. **Q:** {qa.question}")

    return "\n".join(report)