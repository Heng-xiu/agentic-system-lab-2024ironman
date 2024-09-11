import os
from langchain_openai import ChatOpenAI

from app.core.config import settings
from app.agents.search_agent.state import State
from app.agents.search_agent.node.tool import tool

os.environ['OPENAI_API_KEY'] = settings.OPENAI_API_KEY['key']

llm = ChatOpenAI(
    temperature=0,
    max_tokens=512,
    timeout=None,
    max_retries=2,
)

# Modification: tell the LLM which tools it can call
llm_with_tools = llm.bind_tools([tool])

def chatbot(state: State):
    return {"messages": [llm_with_tools.invoke(state["messages"])]}