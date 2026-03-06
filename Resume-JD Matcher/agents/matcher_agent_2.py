from langchain_openai import ChatOpenAI
from core.models import MatchResults  
from core.prompts import matcher_system_prompt, matcher_user_prompt

# Initialize model once at the module level
# Note: You use gpt-5-mini, but ensure your API key supports it!
llm = ChatOpenAI(model="gpt-5-mini", temperature=0)

matcher_agent = llm.with_structured_output(MatchResults)

def get_match_results(resume_json: str, jd_json: str):
    """
    Takes two JSON strings and returns a MatchResults object.
    """
    # Use .format to inject the specific data into your generic prompt
    user_content = matcher_user_prompt.format(
        resume_json=resume_json, 
        jd_json=jd_json
    )
    
    return matcher_agent.invoke([
        ("system", matcher_system_prompt),
        ("user", user_content)
    ])