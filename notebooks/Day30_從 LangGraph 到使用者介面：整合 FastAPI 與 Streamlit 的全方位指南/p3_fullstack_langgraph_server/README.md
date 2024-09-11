# FastAPI LangGraph Streaming Service

## 專案介紹

這個專案是一個基於 FastAPI 的 Web 服務，旨在封裝 LangGraph 並提供高效的串流服務。它採用了生產級別的專案結構，確保了代碼的可維護性和擴展性。

## 用途

本服務主要用於：

1. 封裝 LangGraph 功能，使其易於通過 API 調用。
2. 提供高性能的串流處理能力。
3. 作為一個可擴展的 FastAPI 專案基礎，可以根據需求添加更多功能。

## 安裝說明

1. 克隆此儲存庫：
   ```
   git clone [您的儲存庫 URL]
   cd [專案目錄]
   ```

2. 創建並激活虛擬環境：
   ```
   python -m venv venv
   source venv/bin/activate  # 在 Windows 上使用 `venv\Scripts\activate`
   ```

3. 安裝依賴：
   ```
   pip install -r requirements.txt
   ```

## 啟動伺服器

1. 確保您在專案根目錄下。

2. 設置環境變量（如果需要）：
   ```
   export ENVIRONMENT=development  # 在 Windows 上使用 `set ENVIRONMENT=development`
   ```

3. 運行伺服器：
   ```
   uvicorn app.main:app --reload
   ```

   伺服器將在 `http://localhost:8000` 啟動。

## API 使用說明

1. 訪問 API 文檔：
   打開瀏覽器並訪問 `http://localhost:8000/docs`，您將看到 Swagger UI 文檔。

2. 健康檢查 API：
   - URL: `http://localhost:8000/api/v1/health`
   - Method: GET
   - 響應: `{"status": "OK"}`

3. LangGraph 相關 API：
   (在此添加 LangGraph 相關的 API 端點和使用說明)

## 啟動客戶端
此處提供兩種方式，便於用戶體驗 `invoke` 與 `stream` 差別

啟用方式為
```
呼叫機制
$ streamlit run client_invoke.py
```

```
串流機制
$ streamlit run client_stream.py
```

最後需要使用編寫好的城市來呼叫
```
$ streamlit run streamlit_websearch_app.py
```
## 開發指南

- 所有的路由都應該放在 `app/api/routes/` 目錄下。
- 業務邏輯應該封裝在 `app/services/` 目錄中的服務類中。
- 使用 `app/schemas/` 來定義請求和響應的 Pydantic 模型。
- 配置信息存儲在 `app/core/config.py` 中。
