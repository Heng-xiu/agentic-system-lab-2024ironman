# 說明文件 📘

在這個專案中，包含三個主要部分，分別是 `p0_studio_template` 資料夾、`LangGraph_收集使用者資訊篇.ipynb` 檔案，以及 `p1_gather_user_info` 資料夾。以下是每個部分的介紹與使用說明：

## 1. `p0_studio_template`
這個資料夾是根據 LangGraph Studio 的範例設置，目的是幫助大家熟悉 LangGraph Studio 的使用環境。建議大家先從這個範例開始，建立並熟悉開發環境。

## 2. `LangGraph_收集使用者資訊篇.ipynb`
完成環境設置後，接著使用這個 `.ipynb` 檔案進行實際操作，理解該範例中的情境。這是一個 Jupyter Notebook 檔案，展示了如何使用 LangGraph 來收集使用者資訊，幫助大家更好地掌握相關流程。

## 3. `p1_gather_user_info`
當您了解了前述情境後，可以查看此資料夾內的範例，這部分展示了如何將 Colab 中的程式碼轉換為生產專案。這將幫助您將開發過程順利過渡到 LangGraph Studio 的生產環境中進行操作。

## 使用順序 🗂️

1. **Step 1: 熟悉 LangGraph Studio 環境**
   - 開啟並使用 `p0_studio_template`，建立環境並熟悉 LangGraph Studio 的操作介面。

2. **Step 2: 理解情境**
   - 使用 `LangGraph_收集使用者資訊篇.ipynb`，進行情境模擬，學習如何收集使用者資訊並應用於 LangGraph。

3. **Step 3: 從 Colab 轉換為生產專案**
   - 最後，參考 `p1_gather_user_info`，了解如何將 Colab 中的開發轉換為生產專案，並在 LangGraph Studio 中實現。

---

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
