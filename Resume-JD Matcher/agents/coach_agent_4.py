from langchain_openai import ChatOpenAI
from core.models import CoachResults
from core.prompts import coach_system_prompt, coach_user_prompt


llm = ChatOpenAI(model="gpt-5-mini", temperature=0)
coach_agent = llm.with_structured_output(CoachResults)


def get_coach_results(match_results, ats_results, job_title):
    """Synthesizes all data into a career strategy."""
    user_content = coach_user_prompt.format(
        target_job=job_title,
        match_json=match_results.model_dump_json(),
        ats_json=ats_results.model_dump_json()
    )
    return coach_agent.invoke([
        ("system", coach_system_prompt),
        ("user", user_content)
    ])


