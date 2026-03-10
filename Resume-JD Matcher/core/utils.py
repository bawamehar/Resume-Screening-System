import pdfplumber
from docx import Document
import io



# def print_basic_report(results: MatchResults):
#     print(f"--- MATCH SCORE: {results.match_score}/100 ---")
#     print(f"\n[EXP LOGIC]: {results.experience_reasoning}")
#     print(f"[SKILL LOGIC]: {results.skill_reasoning}")
#     print(f"[PROJECT LOGIC]: {results.project_reasoning}")
#     print(f"[EDUCATION LOGIC]: {results.education_reasoning}")
    
#     print("\n--- MISSING SKILLS (Sorted) ---")
#     for s in results.missing_skills:
#         status = "DEALBREAKER" if s.is_dealbreaker else "Nice-to-have"
#         print(f"- {s.name} (Priority {s.priority}): {status}")
    
#     print(f"\n--- FINAL AUDIT ---\n{results.score_justification}")


# def print_ats_report(results: ATSResults):
#     print(f"--- ATS READABILITY SCORE: {results.ats_score}/100 ---")
#     print(f"\nVERDICT: {results.overall_verdict}")
    
#     print("\nFOUND KEYWORDS:")
#     print(", ".join(results.found_keywords) if results.found_keywords else "None")
    
#     print("\nMISSING KEYWORDS (Critical for Search Ranking):")
#     if results.missing_keywords:
#         for kw in results.missing_keywords:
#             print(f"- {kw}")
#     else:
#         print("All target keywords found!")
        
#     print("\nFORMATTING & STRUCTURE WARNINGS:")
#     if results.formatting_warnings:
#         for warn in results.formatting_warnings:
#             print(f"[{warn.issue_type}] {warn.description}")
#             print(f"    FIX: {warn.fix}")
#     else:
#         print("No major formatting risks detected.")


# def print_coach_report(results: CoachResults):
#     print("="*60)
#     print("🚀 JOB APPLICATION STRATEGY GUIDE")
#     print("="*60)

#     # 1. Resume Enhancements
#     print("\n📝 SECTION 1: RESUME ENHANCEMENTS (STAR METHOD)")
#     print("-" * 45)
#     for i, bullet in enumerate(results.top_3_bullets, 1):
#         print(f"\n💡 Suggestion {i}:")
#         print(f"   [Context]: {bullet.original_context}")
#         print(f"   [Modified]: {bullet.suggested_bullet}")
#         print(f"   [Why]: {bullet.reasoning}")

#     # 2. ATS Optimization
#     print("\n🤖 SECTION 2: ATS QUICK FIXES")
#     print("-" * 45)
#     if results.ats_strategy_points:
#         for point in results.ats_strategy_points:
#             print(f"• {point}")
#     else:
#         print("No specific ATS formatting changes required.")

#     # 3. Interview Preparation
#     print("\n🎤 SECTION 3: TAILORED INTERVIEW PREP")
#     print("-" * 45)
#     for i, qa in enumerate(results.interview_q_and_a, 1):
#         print(f"\n❓ Question {i}: {qa.question}")
#         print(f"   🎯 Intent: {qa.intent}")
#         print(f"   🛡️ Strategy: {qa.strategy}")

#     print("\n" + "="*60)
#     print(f"✨ FINAL NOTE: {results.final_encouragement}")
#     print("="*60)



def extract_text_from_file(uploaded_file):
    """Detects file type and extracts plain text."""
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



# utils.py needs to import blueprint (MatchResults) so it knows 
#exactly what fields it is allowed to print
from core.models import MatchResults, ATSResults, CoachResults


def format_basic_report(results: MatchResults):
    """Formats Agent 2 (MatchResults) using strictly correct schema variables."""
    report = [f"## 🎯 Match Score: {results.match_score}/100"]
    
    report.append("\n### 🧠 Evaluation Logic")
    report.append(f"- **Experience:** {results.experience_reasoning}")
    report.append(f"- **Skills:** {results.skill_reasoning}")
    report.append(f"- **Projects:** {results.project_reasoning}")
    report.append(f"- **Education:** {results.education_reasoning}")
    
    report.append("\n### ❌ Missing Skills & Gaps")
    if results.missing_skills:
        for s in results.missing_skills:
            status = "🚨 **DEALBREAKER**" if s.is_dealbreaker else "💡 Nice-to-have"
            report.append(f"- {s.name} (Priority {s.priority}): {status}")
    else:
        report.append("- No major skill gaps identified!")
        
    report.append(f"\n### 📋 Final Audit Summary\n{results.score_justification}")
    return "\n".join(report)


def format_ats_report(results: ATSResults):
    """Formats Agent 3 (ATSResults) using strictly correct schema variables."""
    report = [f"## 🤖 ATS Readability: {results.ats_score}/100", f"**Verdict:** {results.overall_verdict}\n"]
    
    report.append("### 🚩 Formatting & Structure Warnings")
    if results.formatting_warnings:
        for warn in results.formatting_warnings:
            report.append(f"- **[{warn.issue_type}]**: {warn.description}")
            report.append(f"  *💡 Fix: {warn.fix}*")
    else:
        report.append("- No major formatting risks detected.")
        
    report.append("\n### 🔑 Keyword Analysis")
    found = ", ".join(results.found_keywords) if results.found_keywords else "None"
    report.append(f"- **Found:** {found}")
    
    missing = ", ".join(results.missing_keywords) if results.missing_keywords else "None (All keywords present!)"
    report.append(f"- **Missing:** {missing}")
    
    return "\n".join(report)


def format_coach_report(results: CoachResults):
    """Formats Agent 4 (CoachResults) using strictly correct schema variables."""
    report = ["## 🚀 Job Application Strategy Guide"]
    
    report.append("\n### 📝 Resume Enhancements")
    for i, bullet in enumerate(results.top_3_bullets, 1):
        report.append(f"#### Suggestion {i}")
        report.append(f"- **Context:** {bullet.original_context}")
        report.append(f"- **Modified:** {bullet.suggested_bullet}")
        report.append(f"- **Why:** {bullet.reasoning}\n")

    report.append("### ⚙️ ATS Optimization Quick-Fixes")
    if results.ats_strategy_points:
        for point in results.ats_strategy_points:
            report.append(f"- {point}")
    else:
        report.append("- No specific ATS changes required.")

    report.append("\n### 🎤 Tailored Interview Preparation")
    for i, qa in enumerate(results.interview_q_and_a, 1):
        report.append(f"**Q{i}: {qa.question}**")
        report.append(f"- *Intent:* {qa.intent}")
        report.append(f"- *Strategy:* {qa.strategy}\n")

    report.append(f"\n---\n**✨ Final Note:** {results.final_encouragement}")
    return "\n".join(report)


def format_action_plan(state):
    """Consolidates Match, ATS, and Coach data into a 1-page executive summary."""
    match = state.get("match_results")
    ats = state.get("ats_results")
    coach = state.get("coach_results")
    
    report = []

    # 1. Topline Scores
    report.append(f"## 📊 Quick Assessment")
    report.append(f"**Match Score:** {match.match_score}/100 | **ATS Score:** {ats.ats_score}/100\n")

    # 2. Critical Gaps (Top 3-4 Only)
    report.append("### 🚩 Top Missing Skills")
    if match.missing_skills:
        # Show only dealbreakers or high priority
        gaps = [f"{s.name}" for s in match.missing_skills[:4]]
        report.append(", ".join(gaps))
    
    # if ats:
    #     report.append(f"\n### 🤖 ATS Health Check")
    #     report.append(f"**Verdict:** {ats.overall_verdict}\n")

    # 3. One-Liner Suggestions
    report.append("\n### 💡 Key Resume Edits")
    if coach and coach.top_3_bullets:
        for i, bullet in enumerate(coach.top_3_bullets, 1):
            # Focus only on the 'Suggested' change
            report.append(f"{i}. **Add/Edit:** {bullet.suggested_bullet}")

    # 4. Interview Prep (One-Liners)
    report.append("\n### 🎤 Interview Focus")
    if coach and coach.interview_q_and_a:
        for i, qa in enumerate(coach.interview_q_and_a, 1):
            report.append(f"{i}. **Q:** {qa.question}")

    return "\n".join(report)