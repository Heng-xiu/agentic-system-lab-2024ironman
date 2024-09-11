from app.core.config import settings
from app.agents.search_agent.consts import TOOLS_NODE, CHATBOT_NODE
from app.agents.search_agent.state import State
from app.agents.search_agent.node.chatbot import chatbot
from app.agents.search_agent.node.tool import tool_node

from langgraph.prebuilt import tools_condition
from langgraph.graph import StateGraph, START, END


graph_builder = StateGraph(State)

graph_builder.add_node(CHATBOT_NODE, chatbot)
graph_builder.add_node(TOOLS_NODE, tool_node)

graph_builder.add_edge(START, CHATBOT_NODE)

graph_builder.add_conditional_edges(
    CHATBOT_NODE,
    tools_condition,
)

# Any time a tool is called, we return to the chatbot to decide the next step
graph_builder.add_edge(TOOLS_NODE, CHATBOT_NODE)

graph = graph_builder.compile()