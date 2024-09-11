import os
from app.core.config import settings

from langgraph.prebuilt import ToolNode
from langchain_community.tools.tavily_search import TavilySearchResults

os.environ['TAVILY_API_KEY'] = settings.TAVILY_API_KEY['key']

tool = TavilySearchResults(max_results=2)
tool_node = ToolNode(tools=[tool])