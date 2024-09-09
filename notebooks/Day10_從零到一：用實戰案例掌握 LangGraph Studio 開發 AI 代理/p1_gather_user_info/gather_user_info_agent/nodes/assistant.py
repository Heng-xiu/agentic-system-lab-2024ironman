from typing import Any, Dict, List

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from gather_user_info_agent.state import AssistantGraphState, RequiredInformation

# 初始化語言模型
llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0.7)

# 定義系統提示
system = """你是 AI 客服助理。你的任務是收集必要的用戶資訊。請遵循以下原則:

1. 保持禮貌和專業,使用適當的敬語。
2. 如果用戶詢問的資訊不完整,請適當地要求補充。
3. 在收集用戶資訊時,請確保隱私和安全。
4. 如果無法回答某個問題,請誠實地表示,並提供其他可能的幫助方式。


需要收集的資訊包括：

class RequiredInformation(BaseModel):
    provided_full_name: Optional[str] = Field(
        description="the provided full name of the user"
    )
    provided_mobile: Optional[str] = Field(
        description="the provided mobile number of the user"
    )
    provided_id_4_digits: Optional[int] = Field(
        description="the provided user last 4 digits of id card"
    )

請確保每項資訊都符合要求後再進行下一項。

DO NOT FILL IN THE USERS INFORMATION, YOU NEED TO COLLECT IT.

請根據用戶的問題和已提供的資訊,給出適當的回應和指引。"""

# 創建助理提示模板
assistant_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        (
            "human",
            "User question: {user_question}\n"
            "Chat history: {messages}\n"
            "\n\n What the user have provided so far {provided_required_information} \n\n"
        ),
    ]
)

get_information_chain = assistant_prompt | llm

# 定義助理節點函數
def assistant_chain_func(state: AssistantGraphState) -> Dict[str, Any]:
    get_information_chain = assistant_prompt | llm
    res = get_information_chain.invoke(
        {
            "user_question": state["user_question"],
            "provided_required_information": state["required_information"] if "required_information" in state else RequiredInformation(),
            "messages": state["messages"] if "messages" in state else [],
        }
    )

    # 更新狀態
    updated_state = state.copy()
    updated_state["messages"] = state.get("messages", []) + [res]

    return updated_state