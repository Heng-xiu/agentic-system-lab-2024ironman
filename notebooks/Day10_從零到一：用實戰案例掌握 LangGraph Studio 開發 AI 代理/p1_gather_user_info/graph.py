from langgraph.graph import START, END, StateGraph

from gather_user_info_agent.state import AssistantGraphState
from gather_user_info_agent.consts import ASSISTANT_NODE, COLLECT_INFO_NODE, RESPONSE_BUILDER_NODE
from gather_user_info_agent.nodes.assistant import assistant_chain_func
from gather_user_info_agent.nodes.collect_info import collect_info_chain_func
from gather_user_info_agent.nodes.response_builder import response_builder_func

from gather_user_info_agent.edges.conditional_edges import provided_all_details

from typing import TypedDict, Annotated, Sequence, Literal


# Define the config
class GraphConfig(TypedDict):
    model_name: Literal["openai"]

# Define a new graph
workflow = StateGraph(AssistantGraphState, config_schema=GraphConfig)

# 添加節點
workflow.add_node(ASSISTANT_NODE, assistant_chain_func)
workflow.add_node(COLLECT_INFO_NODE, collect_info_chain_func)
workflow.add_node(RESPONSE_BUILDER_NODE, response_builder_func)


# 添加邊
workflow.add_edge(START, ASSISTANT_NODE )
workflow.add_edge(ASSISTANT_NODE, COLLECT_INFO_NODE)
workflow.add_conditional_edges(
    COLLECT_INFO_NODE,
    provided_all_details,
    {
        "info all collected": RESPONSE_BUILDER_NODE,
        "not fulfill": ASSISTANT_NODE
    }
)
workflow.add_edge(RESPONSE_BUILDER_NODE, END)

# 編譯
graph = workflow.compile()