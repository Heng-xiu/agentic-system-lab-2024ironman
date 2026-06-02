# Contributing to Agentic System Lab 2024 Ironman

感謝你願意協助改進這個專案。本專案是以繁體中文撰寫的 Agentic AI / LangGraph 學習與實作範例庫，目標是讓讀者能從基礎概念一路走到多代理系統、RAG、GraphRAG、觀測、本地模型、FastAPI 與 Streamlit 整合。

這份文件說明如何回報問題、提出 Pull Request，以及維護教學範例時應遵守的基本原則。

## 可以貢獻什麼

歡迎以下類型的貢獻：

* 修正 notebook 無法執行的問題。
* 更新 LangGraph、LangChain、OpenAI SDK 或相關套件的新版本相容性。
* 補充缺漏的環境設定、API key、外部服務或本地模型說明。
* 改善 README、範例導覽、錯字、格式與教學敘述。
* 補上 FastAPI、Streamlit、Ollama、MongoDB、Neo4j、LangFuse 等範例的啟動與驗證步驟。
* 新增小型、聚焦、容易維護的範例。
* 回報過期連結、失效套件、破損圖片或錯誤輸出。
* 協助建立測試、smoke test 或 notebook validation 流程。

請避免一次提交大範圍重寫。這個 repo 的核心價值是「可學、可跑、可維護」。

## 回報 Issue

開 issue 前，請先確認是否已有相似問題。

回報 bug 時，請盡量提供：

* 發生問題的 notebook 或範例路徑。
* 作業系統與 Python 版本。
* 相關套件版本，例如 LangGraph、LangChain、OpenAI SDK。
* 完整錯誤訊息或 traceback。
* 你已經嘗試過的解法。
* 是否使用 OpenAI API、本地 Ollama 模型、MongoDB、Neo4j、LangFuse 或其他外部服務。
* 若問題與 UI 相關，請附截圖或簡短操作步驟。

建議 issue 標題格式：

```text
[Bug] DayXX notebook fails when ...
[Docs] Missing setup steps for ...
[Dependency] Update example for LangGraph ...
[Question] How to run ...
```

## 提交 Pull Request

### 1. Fork 與建立分支

```bash
git clone https://github.com/YOUR_USERNAME/agentic-system-lab-2024ironman.git
cd agentic-system-lab-2024ironman
git checkout -b fix/dayxx-short-description
```

建議分支命名：

```text
fix/day20-mongodb-checkpointer
docs/day26-ollama-setup
chore/update-readme-navigation
examples/day30-streamlit-env
```

### 2. 設定開發環境

本專案目前主要由 notebooks 與範例目錄組成，尚未強制使用單一 dependency lockfile。請依照你要執行的 notebook 或範例安裝需要的套件。

基本 Python 環境可先這樣建立：

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

Windows PowerShell 可使用：

```powershell
python -m venv .venv
.\\.venv\\Scripts\\Activate.ps1
python -m pip install --upgrade pip
```

若 notebook 需要額外服務，請在 PR 中說明你使用的版本與啟動方式，例如：

* Ollama model name 與版本。
* MongoDB 或 Neo4j 連線方式。
* LangFuse / LangSmith 設定。
* FastAPI / Streamlit 啟動指令。
* 需要的環境變數名稱。

不要提交 `.env` 或任何真實 API key。

### 3. 修改原則

請遵守以下原則：

* 優先保持範例簡單、清楚、可教學。
* 不要為了抽象化而讓初學者更難閱讀。
* 修改 notebook 時，盡量讓它能由上到下執行。
* 若無法完整執行，請在 PR 說明原因。
* 若更新套件 API，請補上簡短 migration note。
* 不要提交大型輸出、快取、模型檔、資料庫檔、向量索引或暫存檔。
* 不要提交含有個人資料、私密資料或 API key 的 notebook output。

### 4. 驗證你的修改

文件修改至少執行：

```bash
git diff --check
```

若新增或修改 Python 檔案，請執行：

```bash
python -m compileall .
```

若修改 notebook，請至少手動確認相關 cells 可以執行。若該 notebook 不需要付費 API、外部服務或大型本地模型，建議執行：

```bash
jupyter nbconvert --to notebook --execute path/to/notebook.ipynb --output /tmp/executed-notebook.ipynb
```

若你修改 FastAPI 或 Streamlit 範例，請在 PR 說明你用哪些指令啟動與測試，例如：

```bash
uvicorn app:app --reload
streamlit run app.py
```

實際指令請依範例目錄中的檔名調整。

### 5. PR 描述格式

建議 PR 描述包含：

```markdown
## Summary

- 說明這次改了什麼。

## Affected paths

- `notebooks/DayXX_...`

## Validation

- [ ] Ran `git diff --check`
- [ ] Ran `python -m compileall .`
- [ ] Ran or manually checked the affected notebook
- [ ] Verified related FastAPI / Streamlit example, if applicable

## Notes

- 說明無法驗證的部分、需要的外部服務，或其他維護者需要注意的事項。
```

## Commit message 建議

不強制，但建議使用清楚的 prefix：

```text
docs: improve Day26 Ollama setup notes
fix: update Day20 MongoDB example for current API
chore: add contribution guidelines
examples: simplify Day30 Streamlit startup flow
```

## 文件與語言風格

* 對讀者說明請使用繁體中文。
* 技術名詞、套件名稱、函式名稱與 API 名稱保留英文。
* 寫法以清楚、實用、可執行為優先。
* 避免過度行銷式語氣。
* 若補充說明來自新版官方文件，請附上來源連結。

## 授權

提交 PR 代表你同意你的貢獻會以本專案的 MIT License 釋出。請確認你提交的程式碼、文字、圖片、資料或其他素材有權利被納入此開源專案。

## 維護者回覆時間

這是個人維護的開源教學專案，回覆時間可能不固定。若問題明確、重現步驟完整、PR 範圍小，會更容易被 review 與合併。
