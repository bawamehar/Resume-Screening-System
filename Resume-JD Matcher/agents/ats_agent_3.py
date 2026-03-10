from langchain_openai import ChatOpenAI
from core.models import ATSResults
from core.prompts import ats_system_prompt, ats_user_prompt


llm = ChatOpenAI(model="gpt-5-mini", temperature=0)
ats_agent = llm.with_structured_output(ATSResults)


def get_ats_results(resume_obj, jd_obj):
    # format func injects the data into the placeholders {} defined in prompts file
    user_content = ats_user_prompt.format(
        resume_json=resume_obj.model_dump_json(),
        jd_json=jd_obj.model_dump_json()
    )
    return ats_agent.invoke([
        ("system", ats_system_prompt),
        ("user", user_content)
    ])