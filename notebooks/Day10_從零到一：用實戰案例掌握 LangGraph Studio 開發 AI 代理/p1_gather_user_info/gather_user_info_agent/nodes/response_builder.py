from typing import Any, Dict, List

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# 定義回應建構器的系統提示
response_builder_system = """
你是台灣高鐵的AI客服助理。你的任務是總結對話內容，並提供一個清晰、專業的回應給用戶。請遵循以下原則：

1. 總結已收集的用戶資訊（如果有的話）。
2. 簡要回顧對話中討論的主要問題或請求。
3. 提供任何相關的後續步驟或建議。
4. 使用禮貌和專業的語氣。
5. 如果有任何未完成的事項，請提醒用戶。

請確保你的回應簡潔但全面，並符合高鐵客服的專業標準。
"""

response_builder_prompt = ChatPromptTemplate.from_messages([
    ("system", response_builder_system),
    ("human", "用戶資訊：{user_info}\n對話歷史：{chat_history}\n請提供一個總結性的回應。")
])

llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0.7)

response_chain = response_builder_prompt | llm

def response_builder_func(state: Dict[str, Any]) -> Dict[str, Any]:
    # 提取用戶資訊
    user_info = state.get("required_information", {})
    if hasattr(user_info, 'dict'):
        user_info = user_info.dict()

    # 提取對話歷史
    chat_history = state.get("messages", [])
    chat_history_str = "\n".join([f"{msg.type}: {msg.content}" for msg in chat_history if hasattr(msg, 'type') and hasattr(msg, 'content')])

    # 生成總結回應
    response_chain = response_builder_prompt | llm
    summary_response = response_chain.invoke({
        "user_info": user_info,
        "chat_history": chat_history_str
    })

    # 更新狀態
    updated_state = state.copy()
    updated_state["final_response"] = summary_response.content
    updated_state["messages"] = chat_history + [summary_response]

    return updated_state