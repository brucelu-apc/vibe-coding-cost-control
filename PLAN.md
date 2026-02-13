# Vibe Coding 成本控制執行計劃 (Action Plan)

## 0. 當前問題診斷
*   **現象：** 多專案開發導致 Token 消耗分散，難以統計總支出。
*   **風險：** Vibe Coding 模式下，自動化 Agent 可能在後台產生超預期循環，導致額度快速耗盡。

## 1. 第一階段：建立監控 (Observability)
**目標：讓每一分錢都看得見。**

### 1.1 統一端點 (Unified Endpoint)
*   **動作：** 全面導入 Helicone。
*   **實作：** 
    *   Claude: `https://anthropic.helicone.ai`
    *   Gemini: `https://gateway.helicone.ai` (透過 Target-Url 轉發)
*   **標籤規範：** 必須包含 `Helicone-Property-Project` Header。

### 1.2 數據落庫 (Data Storage)
*   **動作：** 在 Supabase 建立 `cost_logs` 表。
*   **欄位：** `timestamp`, `project_name`, `model`, `tokens_in`, `tokens_out`, `cost_usd`。

## 2. 第二階段：預算管控 (Control)
**目標：設定硬上限，防止爆表。**

### 2.1 每日配額 (Daily Quota)
*   **設定：** 建議初步設定單日上限為 $15 USD（視開發量調整）。
*   **實施：** 使用 LiteLLM Proxy 攔截超過配額的請求。

## 3. 第三階段：成本預估與報告 (Forecasting)
**目標：提前預知帳單金額。**

### 3.1 成本計算腳本
*   **邏輯：** 每天凌晨自動運行。
*   **計算：** `(本月累積消耗 / 已過天數) * 當月總天數`。
*   **輸出：** 推送到 Telegram 給米爸。

---

## 4. 未來優化方向 (Roadmap)
1.  **Prompt 壓縮：** 自動化移除冗長的 Context 以節省 Input Token。
2.  **模型降級策略：** 當日預算消耗超過 70% 時，自動切換到 Flash 等便宜模型進行開發。
