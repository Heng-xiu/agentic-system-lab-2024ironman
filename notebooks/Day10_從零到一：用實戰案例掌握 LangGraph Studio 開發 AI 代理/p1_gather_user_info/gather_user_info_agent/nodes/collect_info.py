from typing import Any, Dict, List
from langchain_core.messages import HumanMessage

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from gather_user_info_agent.state import AssistantGraphState, RequiredInformation

# 使用 OpenAI 模型
llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)

# 資訊收集 Chain
collect_info_system = """你是 AI 客服助理。你的任務是收集必要的用戶資訊。請遵循以下原則:

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

請根據用戶的問題和已提供的資訊,給出適當的回應和指引。
"""

collect_info_prompt = ChatPromptTemplate.from_messages([
    ("system", collect_info_system),
    (
        "human",
        "User question: {user_question}\n"
        "Chat history: {messages}\n"
        "\n\n What the user have provided so far {provided_required_information} \n\n"
    ),
])

collect_info_chain = collect_info_prompt | llm.with_structured_output(RequiredInformation)

## 檢查收集的資訊是否充足
def combine_required_info(info_list: List[RequiredInformation]) -> RequiredInformation:
    info_list = [info for info in info_list if info is not None]

    if len(info_list) == 1:
        return info_list[0]
    combined_info = {}
    for info in info_list:
        for key, value in info.dict().items():
            if value is not None:
                combined_info[key] = value
    return RequiredInformation(**combined_info)

def collect_info_chain_func(state: AssistantGraphState) -> AssistantGraphState:
    """
    收集用戶資訊，驗證，並更新 AssistantGraphState。

    參數:
    state (AssistantGraphState): 當前的助理狀態

    返回:
    AssistantGraphState: 更新後的助理狀態

    說明:
    1. 從標準輸入獲取用戶提供的資訊
    2. 調用 collect_info_chain 處理用戶輸入和當前狀態
    3. 驗證新收集的資訊
    4. 合併新收集的資訊與現有資訊（如果存在）
    5. 更新並返回新的狀態，包括更新後的必要資訊和消息歷史
    """
    # 從標準輸入獲取用戶資訊
    ## #The commented part is because it breaks the UI with the input function
    # information_from_stdin = str(input("\n輸入資訊：\n"))

    information_from_stdin = [HumanMessage(content='我叫李大強，電話號碼：0988168168，身分證末四碼為 8899')]

    # 調用 collect_info_chain 處理用戶輸入
    response = collect_info_chain.invoke(
        {
          "user_question": state["user_question"],
          "provided_required_information": information_from_stdin,
          "messages": state["messages"],
        }
    )

    # 合併新收集的資訊與現有資訊
    if "required_information" in state:
        required_info = combine_required_info(
            info_list=[response, state.get("required_information")]
        )
    else:
        required_info = response

    # 返回更新後的狀態
    return {
        "required_information": required_info,
        "messages": [HumanMessage(content=information_from_stdin)],
    }