from pydantic_settings import BaseSettings
import json 
from typing import Dict
from pathlib import Path

THIS_DIR = Path(__file__).parent.parent.parent
print(f"THIS_DIR{THIS_DIR}")
class Settings(BaseSettings):
    # API 設置
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "2024 年用 LangGraph 從零開始實現 Agentic AI System"

    class Config:
        # 通过 Pydantic config 来指示模型应如何解析和加载环境变量
        env_file = Path(THIS_DIR, ".env"), 
        env_file_encoding = 'utf-8'
        json_encoders = {
            dict: json.dumps  
        }
    
    OPENAI_API_KEY: Dict[str, str] = {
        "key": "OPENAI_API_KEY",
    }
    TAVILY_API_KEY:Dict[str, str] = {
        "key": "TAVILY_API_KEY",
    }

settings = Settings()