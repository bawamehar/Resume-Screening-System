from langgraph.graph import StateGraph, END
from core.models import AgentState
from agents.parser_agent_1 import get_parsed_data
from agents.matcher_agent_2 import get_match_results

# 1. Define the Nodes
def node_parse_data(state: AgentState):
    """Agent 1: Logic"""
    res = get_parsed_data("Resume", state['raw_resume'])
    jd = get_parsed_data("Job Description", state['raw_jd'])
    return {"resume_obj": res, "jd_obj": jd}

def node_match_data(state: AgentState):
    """Agent 2: Logic"""
    results = get_match_results(state['resume_obj'], state['jd_obj'])
    return {"match_results": results}

# 2. Build the Graph
workflow = StateGraph(AgentState)
workflow.add_node("parser", node_parse_data)
workflow.add_node("matcher", node_match_data)

# 3. Define the Flow
workflow.set_entry_point("parser")
workflow.add_edge("parser", "matcher")
workflow.add_edge("matcher", END)

app = workflow.compile()