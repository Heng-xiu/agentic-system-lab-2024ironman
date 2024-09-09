from typing import Literal
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI

from gather_user_info_agent.state import AssistantGraphState, RequiredInformation

# 資料模型
class RouteQuery(BaseModel):
    """將使用者查詢路由到最相關的處理節點。"""

    route_to: Literal["common_questions", "small_talk"] = Field(
        ...,
        description="根據使用者問題選擇路由到常見問題處理或閒聊處理。",
    )

# 使用 LLM 進行函式呼叫
llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)
structured_llm_router = llm.with_structured_output(RouteQuery)

# 提示模板
system = """你是高鐵客服機器人的路由專家。你的任務是將使用者的問題分類為以下兩類之一：
1. 常見問題（common_questions）：與高鐵服務、票務、行程等相關的問題。
2. 閒聊（small_talk）：與高鐵無直接關係的一般性對話或問候。

如果問題屬於高鐵相關的常見問題，請選擇 'common_questions'。
如果問題是一般性的閒聊或與高鐵無關，請選擇 'small_talk'。"""

route_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "{question}"),
    ]
)

question_router = route_prompt | structured_llm_router

def route_query_to_common_questions_and_small_talk(state: AssistantGraphState)  -> Literal["common_questions", "small_talk"]:
    """替使用者問題進行分類"""
    question = state["user_question"]
    result = question_router.invoke({"question": question})
    print(f"路由結果: {result}")
    if result.route_to == "common_questions":
        return "common_questions"
    else:
        return "small_talk"

def provided_all_details(state: AssistantGraphState) -> Literal["info all collected", "not fulfill"]:
    if "required_information" not in state:
        return "not fulfill"
    provided_information: RequiredInformation = state["required_information"]
    if (
        provided_information.provided_full_name
        and provided_information.provided_mobile
        and provided_information.provided_id_4_digits
    ):
        return "info all collected"

    else:
        return "not fulfill"