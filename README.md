# 2024 年用 LangGraph 從零開始實現 Agentic AI System

歡迎來到 Agentic System Lab! 這個專案是為 [2024 年 iThome 鐵人賽](https://ithelp.ithome.com.tw/users/20161074/ironman/7469)準備的，專注於探索 AI 代理系統的前沿技術。

## 專案簡介

本專案旨在通過 30 天的系列文章,深入探討 Agentic System 的各個方面，從基礎概念到實際應用。我們將特別關注 LangGraph 框架，並探索多代理系統的設計和實現。

## 內容概覽

- AI 代理系統的基本概念和演進
- LangGraph 框架深度解析
- 多代理系統的設計模式和應用
- 相關工具介紹: LangGraph Studio, LangFuse, Ollama, DSPy

## 檔案結構

```
.
├── README.md
├── notebooks/
│   ├── day1_introduction.ipynb
│   ├── day2_langgraph_basics.ipynb
│   └── ...
└── resources/
    ├── images/
    └── data/
```

## 使用指南

1. 克隆此 repository:
   ```
   git clone https://github.com/Heng-xiu/agentic-system-lab-2024ironman.git
   ```

2. 瀏覽 `notebooks/` 目錄以查看每日的教學內容和程式碼範例。

## 系列文章連結

根據每日發文次序，將內容連結更新上來，方便大家點選
| 日期 | 文章標題 | 摘要 |
| ---- | ---- | ---- |
| Day1 | [Agentic System 探索之旅](https://ithelp.ithome.com.tw/articles/10346355) | 展開探索旅程 |
| Day2 | [什麼是 AI 代理？複合式 AI 與 Agentic AI 的創新之路](https://ithelp.ithome.com.tw/articles/10346976) | 文章深入探討了人工智慧領域從單一模型到複合式 AI 系統的轉變，並重點介紹了 AI 代理 的概念和應用。 |
| Day3 | [LangGraph：構建下一代智能應用的革命性框架](https://ithelp.ithome.com.tw/articles/10347050) | LangGraph 以圖形結構為基礎，將每個 AI 代理視為節點，而代理之間的資訊傳遞則以邊來呈現。它提供狀態管理功能，讓代理能夠在執行任務時更新自身的狀態，並保持上下文連貫性。 |
| Day4 | [LangGraph 入門教程：節點、邊、狀態](https://ithelp.ithome.com.tw/articles/10347138) | 文章展示了如何使用 LangGraph 的核心元件（節點、邊和狀態）來建構一個簡單的天氣查詢代理，並強調了 LangGraph 在構建智能系統方面的潛力。 |
| Day5 | [LangChain 與 LangGraph 串流技術深度探索](https://ithelp.ithome.com.tw/articles/10347147) | 展示了 LangChain 與 LangGraph 的串流功能，旨在說明如何以分段式輸出和事件串流的方式提升基於大型語言模型 (LLM) 應用程式的效能。 |
| Day6 |  [LangChain 與 LangGraph 工具實戰探討：AI 模型的程式呼叫能力](https://ithelp.ithome.com.tw/articles/10347269) | 探討了 LangChain 和 LangGraph 能夠賦予 AI 模型呼叫外部程式碼的能力，進而擴展其功能並實現更智能的交互。文章首先介紹了「工具」的概念，並說明其如何充當 AI 模型與外部世界溝通的橋樑。 |
| Day7 | [LangGraph 深入探索：Tool Calling 機制與進階應用](https://ithelp.ithome.com.tw/articles/10347297) | 本文探討 LangGraph 框架中的 ToolCalling 技術，它是一種讓大型語言模型 (LLM) 能夠與外部工具互動的機制。文章首先介紹 ToolCalling 的核心概念和關鍵特性，像是動態互動、能力擴展和靈活性。 |
| Day8 | [深入理解LangGraph狀態的工作機制](https://ithelp.ithome.com.tw/articles/10347304) | 以大家熟悉的「大地遊戲」為比喻，深入淺出地解說了 LangGraph 的狀態管理機制，並強調其在 AI 對話系統中的重要性。 |
| Day9 | [從 Redux 到 LangGraph：AI 時代下的狀態管理新思維](https://ithelp.ithome.com.tw/articles/10347417) | 文章主要探討了兩種狀態管理框架：傳統的 Redux 和新興的 LangGraph，並比較了它們的設計理念和應用場景。 |
| Day10 | [從零到一：用實戰案例掌握 LangGraph Studio 開發 AI 代理](https://ithelp.ithome.com.tw/articles/10348545) | 文章詳細說明了使用 LangGraph Studio 的準備工作，包括系統需求、必要軟體和開發環境。文章還提供了一個步驟式的教學，指導讀者如何設定和使用 LangGraph Studio |
| Day11 | [從反思到監督:五大 AI 代理設計模式速成指南](https://ithelp.ithome.com.tw/articles/10348572) | 介紹了五種 AI 代理設計模式，分別是：反思（Reflection）、反饋學習（Reflexion）、規劃（Planning）、監督者（Supervisor）和協作（Collaboration）。這些設計模式展示了 AI 系統在自我優化、強化學習、自主規劃和協同工作方面的巨大潛力。 |
| Day12 | [AI代理自我反思：深入探討 Self-Refine 技術與 LangGraph 實作](https://ithelp.ithome.com.tw/articles/10348596) | 這篇文章介紹了大型語言模型 (LLM) 的自我完善技術，特別是 Self-Refine 的概念和實作方法。它解釋了 Self-Refine 的工作原理，包含問題識別、建議生成和程式碼重寫三個步驟，並展示了其相較於傳統方法的優勢。最後，文章透過 LangGraph 示範了 Self-Refine 的應用，並展望了 LLM 自我完善技術的未來發展。 |
| Day13 | [進階 LLM 反思機制：Reflexion 技術的創新與應用](https://ithelp.ithome.com.tw/articles/10348597) | 這篇文章探討了 Reflexion 技術，透過記憶機制、多步推理和動態任務適應來克服 Self-Refine 的局限。文章詳細解說了 Reflexion 的核心架構，並展示其在 AI 從錯誤中學習並持續改進的實際應用。最後，文章強調 Reflexion 對於推動 AI 自主性和智能化發展的重要性。 |
| Day14 | [翻譯革新：從吳恩達的 Translation Agent 到 LangGraph 的智能協作模式](https://ithelp.ithome.com.tw/articles/10348599) | 這篇文章探討了機器翻譯領域的最新進展，特別是 Translation Agent 和 LangGraph 兩個工具如何提升翻譯效率和準確性。Translation Agent 透過反思工作流模擬人類譯者的思考過程，分為初始翻譯、反思與改進、優化輸出三步驟。文章最後展望了機器翻譯技術的未來發展，如探索更多語言模型及新翻譯質量指標。 |
| Day15 | [Agentic Design Pattern: Planning - 賦予 AI 自主規劃能力](https://ithelp.ithome.com.tw/articles/10348600) | 這篇文章介紹了 Agentic Design Pattern 中的 Planning 模式，賦予 AI 自主規劃複雜任務的能力。它還探討了 Plan-and-Solve 論文，說明如何讓大型語言模型制定計劃並生成推理過程。最後，文章展示了使用 LangChain 和 LangGraph 實現這些方法的步驟和效果。 |
| Day16 | [Agentic Pattern：以多代理協作模式革新 AI 系統](https://ithelp.ithome.com.tw/articles/10348601) | 這篇文章探討了多代理系統在人工智能中的應用，並介紹了如何利用 LangGraph 框架來構建和管理這些系統。文章闡述了協作模式和監督者模式兩種常見的設計方式，並以多代理協作翻譯系統為例，展示了具體實作。最後，文章總結了多代理系統的優勢，並鼓勵讀者利用 LangGraph 來構建更複雜的 AI 系統。 |
| Day17 | [多代理系統設計: 監督者模式的應用與實踐](https://ithelp.ithome.com.tw/articles/10348602) | 這篇文章探討了多代理系統設計中的監督者模式，並以台灣棒球和啦啦隊新聞處理系統為例進行實踐展示。該系統包含多個 AI 代理，由監督者代理進行協調管理。文章最後強調了監督者模式的優勢，並探討了未來的改進方向。|
| Day18 | [LangGraph 與 LangFuse：打造 Agent 觀測系統全方位指南](https://ithelp.ithome.com.tw/articles/10348794) | 這篇文章介紹了如何使用 LangGraph 與 LangFuse 打造全方位的 Agent 觀測系統。LangGraph 用於構建複雜的 AI 代理應用，而 LangFuse 則提供監控、分析和優化功能。文章透過程式碼範例和視覺化工具，展示如何建立更智能且高效的 AI 應用程式。 |
| Day19 | [LangGraph 的記憶機制：提升 AI 助理的上下文理解能力](https://ithelp.ithome.com.tw/articles/10348818) | 這篇文章探討了 LangGraph 框架如何提升 AI 助理的記憶能力，並有效管理對話歷史。文章介紹了 LangGraph 的核心機制 Checkpointer，作為 AI 的記憶儲存器，能捕捉並儲存圖形的完整狀態。最後，文章總結了透過 LangGraph 來提升 AI 助理記憶能力和管理對話上下文的關鍵優點。 |
| Day20 | [結合 LangGraph 與 MongoDB 打造智慧工地安全監控系統：Agentic RAG 技術應用實例](https://ithelp.ithome.com.tw/articles/10349091) | 這篇文章探討了如何將 LangGraph 與 MongoDB 結合，打造智慧工地安全監控系統，並介紹了 LangGraph 的 Checkpointer 機制與 MongoDB 的資料儲存功能。文章展示了如何使用 OpenAI 嵌入模型將文字轉換為向量，並利用 MongoDB 的 $vectorSearch 進行語意搜尋，快速找到相關的安全事件記錄。最後，文章強調透過整合 LangGraph 工作流和 MongoDB，系統能即時分析並持久儲存資料，應用範圍廣泛。 |
| Day21 | [從基礎到進階: 掌握RAG基礎並使用LangGraph 實現 Agentic RAG](https://ithelp.ithome.com.tw/articles/10348870) | 文章探討了檢索增強生成 (RAG) 技術，結合資訊檢索和文本生成以克服大型語言模型的局限性。文章介紹了 RAG 的核心組成部分及其應用場景，並強調其在降低系統建置成本方面的優勢。最後，文章展示了如何使用 LangGraph 框架構建一個 Agentic RAG 系統來回答使用者問題。 |
| Day22 | [CRAG: 檢索增強生成的糾錯機制 - 提升大型語言模型問答精確度](https://ithelp.ithome.com.tw/articles/10348884) | 這篇文章介紹了「Corrective RAG (CRAG)」技術，旨在提升大型語言模型（LLM）在問答系統中的準確性與可靠性。CRAG 通過「檢索評估器」和「知識精練」兩大機制優化檢索結果，克服傳統 RAG 模型在資訊相關性和品質上的局限。文章還展示了如何利用 LangGraph 框架構建一個基於 CRAG 的問答系統，並展示其實際應用效果。 |
| Day23 | [Adaptive-RAG：動態檢索策略提高系統問答精準度](https://ithelp.ithome.com.tw/articles/10348895) | 這篇文件介紹了「Adaptive-RAG」技術，旨在提升問答系統的準確性和效率。Adaptive-RAG 透過動態調整檢索方法，根據查詢複雜度選擇最佳策略，簡單查詢直接生成答案，複雜查詢則採用多步檢索和推理策略。文件詳細描述了其核心組件、訓練方法與效能分析，並總結其革新意義與未來應用潛力。 |
| Day24 | [GraphRAG：革新檢索增強生成的新範式](https://ithelp.ithome.com.tw/articles/10348910) | 這篇文章介紹了微軟研究團隊提出的 GraphRAG 技術，旨在解決傳統 RAG 在處理複雜資訊時的局限。GraphRAG 通過將文本轉化為知識圖譜並利用社群層級摘要，增強了大型語言模型的推理和語義理解能力。文章還詳細討論了 GraphRAG 的索引和查詢機制，並展示其在處理複雜查詢時的優勢。 |
| Day25 | [數位轉型下的工安革命：知識圖譜與LangGraph的完美結合](https://ithelp.ithome.com.tw/articles/10348921) | 這篇文章探討了結合知識圖譜與 LangGraph 來打造智慧工安監控系統的方式，強調了知識圖譜在儲存結構化與非結構化資料及複雜關係分析上的優勢。文章展示了如何使用 Neo4j 構建知識圖譜並導入工安事件資料，並利用 LangGraph 編織智能工作流以提供精確查詢結果。最後，文章強調了知識圖譜、LangGraph 和 RAG 的結合，為工地安全監控帶來變革。 |
| Day26 | [Ollama: 革命性工具讓本地 AI 開發觸手可及 - 從安裝到進階應用的完整指南](https://ithelp.ithome.com.tw/articles/10348913) | 這篇文章是關於 Ollama 的詳細指南，介紹了其作為開源本地大型語言模型運行框架的特性和優點。文章涵蓋了 Ollama 的安裝、啟動、API 呼叫等步驟，以及在 Docker 和 Colab 中部署的方法。最後，文章強調了 Ollama 的進階應用，並鼓勵讀者探索其在本地 AI 開發中的潛力。 |
| Day27 | [告別提示工程：DSPy如何革新大型語言模型的應用開發](https://ithelp.ithome.com.tw/articles/10348919) | DSPy 是由 Stanford NLP 研究人員開發的框架，旨在簡化大型語言模型 (LLM) 的開發，強調以編程而非提示設計來控制模型。它使用「Signatures」定義任務、「Modules」組合 LLM 行為，並使用「Optimizers」自動調整提示以優化性能。這些元素的結合讓開發者能以更系統化和高效的方式開發 LLM 應用程式並提高模型性能。|
| Day28 | [從零開始的 DSPy：打造高效翻譯錯誤檢測系統](https://ithelp.ithome.com.tw/articles/10348920) | 這篇文章介紹了 DSPy AI 開發框架，展示其如何幫助開發者更有效地構建和優化語言模型。文章以翻譯錯誤檢測任務為例，詳細介紹了 DSPy 的功能模塊和自動優化技術，並通過圖表和程式碼示例展示性能提升。最後，文章強調了 DSPy 在簡化開發流程和提升模型性能方面的重要性。 |
| Day29 | [網站開發遇上 AI：FastAPI、Streamlit 與 LangServe 的實戰指南](https://ithelp.ithome.com.tw/articles/10348922) | 這篇文章旨在教讀者如何使用 FastAPI 建構後端服務，利用 Streamlit 打造互動式前端介面，並通過 LangServe 整合 LangChain 模型，最終實現智慧笑話生成器。文章結構清晰，涵蓋環境設定、後端與前端開發以及 AI 模型整合，並提供詳細的程式碼範例和圖示說明。文章為讀者提供全面的學習指南，幫助快速掌握 AI 驅動應用的核心技能，並激發 AI 領域的創新機會。 |
| Day30 | [從 LangGraph 到使用者介面：整合 FastAPI 與 Streamlit 的全方位指南](https://ithelp.ithome.com.tw/articles/10348923) | 這篇文章首先介紹了專案的核心目標，包括理解自然語言查詢、進行即時網路搜尋和支援多輪對話。接著，文章詳細分析了系統架構，將其分為前端、後端和核心處理層，並介紹了 LangGraph、FastAPI 和 Streamlit 的使用。後半部分深入探討了 LangGraph 的實作，展示了其圖形結構、狀態管理及與前後端的整合如何構建複雜的對話系統並提供流暢的使用體驗。|
| Day31 | [忙碌上班族如何在鐵人賽中堅持30天寫作？從靈感到策略：9個關鍵步驟](https://ithelp.ithome.com.tw/articles/10358571) | 這篇文章記錄了作者參加 30 天寫作挑戰的過程和心得。作者從挑戰的動機和目的出發，詳細闡述了自身在設定目標、時間管理、克服瓶頸以及提升寫作效率等方面的策略和經驗。文章分為九個章節，分別介紹了作者的寫作挑戰動機、挑戰的過程、遇到的困難、解決方案、使用的工具、寫作瓶頸的克服以及成果和反思。最後，作者呼籲讀者也參與類似的寫作挑戰，並分享了一些實用的建議和資源。文章的主旨是在於鼓勵讀者持續寫作，透過寫作來提升自我，並在寫作的過程中獲得成長和收穫。 |

## Star 趨勢

[![Star History Chart](https://api.star-history.com/svg?repos=Heng-xiu/agentic-system-lab-2024ironman&type=Date)](https://star-history.com/#Heng-xiu/agentic-system-lab-2024ironman&Date)

## 貢獻指南

我們歡迎社群貢獻! 如果您有任何改進建議或發現了 bug,請提交 issue 或 pull request。

## 授權信息

本專案採用 MIT 授權。詳情請見 [LICENSE](LICENSE) 文件。

---

如果您覺得這個專案有幫助,請給我們一個星星 ⭐️ 並分享給您的朋友!
