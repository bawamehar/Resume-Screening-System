from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from models import ExtractedData
from prompts import system_prompt, user_prompt


# Initialize the model once
# Setup the Agent 
llm = ChatOpenAI(model="gpt-5-mini", temperature=0)

# Binding the schema to the LLM
parser_agent = llm.with_structured_output(ExtractedData)

def get_parsed_data(doc_type, raw_text):

    parser_prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt), 
        ("user", user_prompt)
    ])

    # 2. Chain them together
    # This is the "LangChain" way: Prompt -> Model -> Structured Output
    parser_chain = parser_prompt | parser_agent 


    #resume_data = parser_chain.invoke(resume_input)
    #jd_data = parser_chain.invoke(jd_input)

    # print("--- RESUME DATA ---")
    # print(resume_data.model_dump_json(indent=2))
    # print("\n--- JD DATA ---")
    # print(jd_data.model_dump_json(indent=2))
    
    
    return parser_chain.invoke({"doc_type": doc_type, "raw_text": raw_text})