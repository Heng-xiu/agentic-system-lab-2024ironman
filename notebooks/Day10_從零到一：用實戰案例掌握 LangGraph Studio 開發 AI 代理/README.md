# 說明文件 📘

在這個專案中，主要包含兩個資料夾，分別是 `p0_studio_template` 和 `p1_gather_user_info`，以下是每個資料夾的介紹與使用說明：

## 1. `p0_studio_template`
這個資料夾是根據 LangGraph Studio 的範例進行設置，主要用途是幫助大家建置開發環境，並且熟悉如何在 LangGraph Studio 中進行操作。請參照此範例進行環境配置，來了解 LangGraph Studio 的各項功能。

## 2. `p1_gather_user_info`
此資料夾提供了一個實際範例，展示了如何將 Colab 的程式碼轉換為生產專案，並提供給 LangGraph Studio 進行操作。這裡可以讓大家了解如何從開發環境轉移到生產應用環境。請多次回到相關文章中進行反覆觀察，以便更好理解整個過程。

## 使用說明 ⚙️

1. **記得 clone 專案：**
   透過 Git 將專案 clone 到本地端進行操作。

   ```bash
   git clone https://github.com/your-repo/langgraph-project.git
   ```

2. **下載並安裝 LangGraph Studio：**
   請至 LangGraph Studio 官方網站下載並安裝對應的 IDE 工具，以確保您可以在本地端執行範例程式碼。

3. **設定 `.env` 檔案：**
   將範例 `.env.example` 檔案複製一份並命名為 `.env`。接著，將您的 API Key 填入該檔案中，確保系統能夠正常運行。

   ```bash
   cp .env.example .env
   ```

   然後，打開 `.env` 檔案，將您的 API Key 補充進去：

   ```bash
   OPENAI_API_KEY=sk-xxxx
   LANGCHAIN_API_KEY=sk-xxxx
   TAVILY_API_KEY=tvly-xxxx
   ```

4. **確認環境配置正確：**
   在 `.env` 檔案中正確配置您的 API Key 後，您即可透過 LangGraph Studio 運行範例專案，開始體驗 AI 代理的開發與操作流程。

---

如果您在過程中遇到問題，請回到文章進行詳細觀察，並確保您已正確設定環境。
