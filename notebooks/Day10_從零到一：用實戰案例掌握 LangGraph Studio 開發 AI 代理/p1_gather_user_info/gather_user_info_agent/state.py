from typing import Annotated, Optional, TypedDict

from langchain_core.pydantic_v1 import BaseModel, Field
from langgraph.graph import add_messages

## 定義使用者資訊
class RequiredInformation(BaseModel):
    provided_full_name: Optional[str] = Field(
        description="使用者提供的全名"
    )
    provided_mobile: Optional[str] = Field(
        description="使用者提供的台灣電話號碼"
    )
    provided_id_4_digits: Optional[int] = Field(
        description="使用者提供的身分證末四碼"
    )


## 定義 Graph 中狀態管理
class AssistantGraphState(TypedDict):
    user_question: str
    required_information: RequiredInformation
    messages: Annotated[list, add_messages]
    verified: bool