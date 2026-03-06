# utils.py needs to import blueprint (MatchResults) so it knows 
# #exactly what fields it is allowed to print
from core.models import MatchResults


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
