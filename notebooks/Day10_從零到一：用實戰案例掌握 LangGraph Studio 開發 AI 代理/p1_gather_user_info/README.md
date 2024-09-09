# p1_gather_user_info

這個項目是一個用戶信息收集系統，使用 LangGraph 框架實現。

## 項目結構

```
p1_gather_user_info
├── README.md
├── gather_user_info_agent
│   ├── __init__.py
│   ├── consts.py
│   ├── edges
│   │   └── conditional_edges.py
│   ├── nodes
│   │   ├── __init__.py
│   │   ├── assistant.py
│   │   ├── collect_info.py
│   │   ├── response_builder.py
│   └── state.py
├── graph.py
├── langgraph.json
└── requirements.txt
```

## 主要組件

- `gather_user_info_agent/`: 主要的代理邏輯
  - `consts.py`: 定義常量
  - `edges/`: 包含條件邊的邏輯
  - `nodes/`: 包含各種節點的實現
    - `assistant.py`: 助手節點
    - `collect_info.py`: 信息收集節點
    - `response_builder.py`: 響應生成節點
  - `state.py`: 定義狀態管理

- `graph.py`: 定義整個圖結構
- `langgraph.json`: LangGraph 配置文件
- `requirements.txt`: 項目依賴
