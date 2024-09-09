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

每日更新的文章連結將會在這裡列出:

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
| Day12 | AI代理自我反思：深入探討 Self-Refine 技術與 LangGraph 實作 | 這篇文章介紹了大型語言模型 (LLM) 的自我完善技術，特別是 Self-Refine 的概念和實作方法。它解釋了 Self-Refine 的工作原理，包含問題識別、建議生成和程式碼重寫三個步驟，並展示了其相較於傳統方法的優勢。最後，文章透過 LangGraph 示範了 Self-Refine 的應用，並展望了 LLM 自我完善技術的未來發展。 |
| Day13 | 進階 LLM 反思機制：Reflexion 技術的創新與應用 | 這篇文章探討了 Reflexion 技術，透過記憶機制、多步推理和動態任務適應來克服 Self-Refine 的局限。文章詳細解說了 Reflexion 的核心架構，並展示其在 AI 從錯誤中學習並持續改進的實際應用。最後，文章強調 Reflexion 對於推動 AI 自主性和智能化發展的重要性。 |
| Day14 | 翻譯革新：從吳恩達的 Translation Agent 到 LangGraph 的智能協作模式 | 這篇文章探討了機器翻譯領域的最新進展，特別是 Translation Agent 和 LangGraph 兩個工具如何提升翻譯效率和準確性。Translation Agent 透過反思工作流模擬人類譯者的思考過程，分為初始翻譯、反思與改進、優化輸出三步驟。文章最後展望了機器翻譯技術的未來發展，如探索更多語言模型及新翻譯質量指標。 |
| Day15 | Agentic Design Pattern: Planning - 賦予 AI 自主規劃能力 | 這篇文章介紹了 Agentic Design Pattern 中的 Planning 模式，賦予 AI 自主規劃複雜任務的能力。它還探討了 Plan-and-Solve 論文，說明如何讓大型語言模型制定計劃並生成推理過程。最後，文章展示了使用 LangChain 和 LangGraph 實現這些方法的步驟和效果。 |
| Day16 | Agentic Pattern：以多代理協作模式革新 AI 系統 | 這篇文章探討了多代理系統在人工智能中的應用，並介紹了如何利用 LangGraph 框架來構建和管理這些系統。文章闡述了協作模式和監督者模式兩種常見的設計方式，並以多代理協作翻譯系統為例，展示了具體實作。最後，文章總結了多代理系統的優勢，並鼓勵讀者利用 LangGraph 來構建更複雜的 AI 系統。 |
| Day17 | 多代理系統設計: 監督者模式的應用與實踐 | 這篇文章探討了多代理系統設計中的監督者模式，並以台灣棒球和啦啦隊新聞處理系統為例進行實踐展示。該系統包含多個 AI 代理，由監督者代理進行協調管理。文章最後強調了監督者模式的優勢，並探討了未來的改進方向。|
| Day18 | 待定 | 待定 |

## 貢獻指南

我們歡迎社群貢獻! 如果您有任何改進建議或發現了 bug,請提交 issue 或 pull request。

## 授權信息

本專案採用 MIT 授權。詳情請見 [LICENSE](LICENSE) 文件。

---

如果您覺得這個專案有幫助,請給我們一個星星 ⭐️ 並分享給您的朋友!
