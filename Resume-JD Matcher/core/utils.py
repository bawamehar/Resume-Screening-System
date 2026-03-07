# utils.py needs to import blueprint (MatchResults) so it knows 
# #exactly what fields it is allowed to print
from core.models import MatchResults, ATSResults


def print_basic_report(results: MatchResults):
    print(f"--- MATCH SCORE: {results.match_score}/100 ---")
    print(f"\n[EXP LOGIC]: {results.experience_reasoning}")
    print(f"[SKILL LOGIC]: {results.skill_reasoning}")
    print(f"[PROJECT LOGIC]: {results.project_reasoning}")
    print(f"[EDUCATION LOGIC]: {results.education_reasoning}")
    
    print("\n--- MISSING SKILLS (Sorted) ---")
    for s in results.missing_skills:
        status = "DEALBREAKER" if s.is_dealbreaker else "Nice-to-have"
        print(f"- {s.name} (Priority {s.priority}): {status}")
    
    print(f"\n--- FINAL AUDIT ---\n{results.score_justification}")


def print_ats_report(results: ATSResults):
    print(f"--- ATS READABILITY SCORE: {results.ats_score}/100 ---")
    print(f"\nVERDICT: {results.overall_verdict}")
    
    print("\nFOUND KEYWORDS:")
    print(", ".join(results.found_keywords) if results.found_keywords else "None")
    
    print("\nMISSING KEYWORDS (Critical for Search Ranking):")
    if results.missing_keywords:
        for kw in results.missing_keywords:
            print(f"- {kw}")
    else:
        print("All target keywords found!")
        
    print("\nFORMATTING & STRUCTURE WARNINGS:")
    if results.formatting_warnings:
        for warn in results.formatting_warnings:
            print(f"[{warn.issue_type}] {warn.description}")
            print(f"    FIX: {warn.fix}")
    else:
        print("No major formatting risks detected.")

