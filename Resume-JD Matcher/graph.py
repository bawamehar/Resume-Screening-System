from langgraph.graph import StateGraph, END
from core.models import AgentState
from agents.parser_agent_1 import get_parsed_data
from agents.matcher_agent_2 import get_match_results
from agents.ats_agent_3 import get_ats_results
from agents.coach_agent_4 import get_coach_results


# Define the Nodes
def node_parse_data(state: AgentState):
    """Agent 1: Logic"""
    res = get_parsed_data("Resume", state['raw_resume'])
    jd = get_parsed_data("Job Description", state['raw_jd'])
    return {"resume_obj": res, "jd_obj": jd}

def node_match_data(state: AgentState):
    """Agent 2: Logic"""
    results = get_match_results(state['resume_obj'], state['jd_obj'])
    return {"match_results": results}

def node_ats_audit(state: AgentState):
    """Agent 3: ATS Readability and Keyword Audit"""
    results = get_ats_results(state["resume_obj"], state["jd_obj"])
    return {"ats_results": results}

def node_coach_strategy(state: AgentState):
    """Agent 4: Career Coach Synthesis"""
    job_title = state["jd_obj"].job_title 
    
    results = get_coach_results(
        state["match_results"], 
        state["ats_results"], 
        job_title
    )
    return {"coach_results": results}


# Build the Graph
workflow = StateGraph(AgentState)
workflow.add_node("parser", node_parse_data)
workflow.add_node("matcher", node_match_data)
workflow.add_node("ats_node", node_ats_audit)
workflow.add_node("coach_node", node_coach_strategy)


# Define the Flow
workflow.set_entry_point("parser")
workflow.add_edge("parser", "matcher")
workflow.add_edge("matcher", "ats_node") 
workflow.add_edge("ats_node", "coach_node")
workflow.add_edge("coach_node", END)


app = workflow.compile()