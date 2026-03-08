# utils.py needs to import blueprint (MatchResults) so it knows 
# #exactly what fields it is allowed to print
from core.models import MatchResults, ATSResults, CoachResults


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


def print_coach_report(results: CoachResults):
    print("="*60)
    print("🚀 JOB APPLICATION STRATEGY GUIDE")
    print("="*60)

    # 1. Resume Enhancements
    print("\n📝 SECTION 1: RESUME ENHANCEMENTS (STAR METHOD)")
    print("-" * 45)
    for i, bullet in enumerate(results.top_3_bullets, 1):
        print(f"\n💡 Suggestion {i}:")
        print(f"   [Context]: {bullet.original_context}")
        print(f"   [Modified]: {bullet.suggested_bullet}")
        print(f"   [Why]: {bullet.reasoning}")

    # 2. ATS Optimization
    print("\n🤖 SECTION 2: ATS QUICK FIXES")
    print("-" * 45)
    if results.ats_strategy_points:
        for point in results.ats_strategy_points:
            print(f"• {point}")
    else:
        print("No specific ATS formatting changes required.")

    # 3. Interview Preparation
    print("\n🎤 SECTION 3: TAILORED INTERVIEW PREP")
    print("-" * 45)
    for i, qa in enumerate(results.interview_q_and_a, 1):
        print(f"\n❓ Question {i}: {qa.question}")
        print(f"   🎯 Intent: {qa.intent}")
        print(f"   🛡️ Strategy: {qa.strategy}")

    print("\n" + "="*60)
    print(f"✨ FINAL NOTE: {results.final_encouragement}")
    print("="*60)
