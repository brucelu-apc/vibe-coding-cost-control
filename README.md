# Vibe Coding 成本控制專案 (Vibe Coding Cost Control)

本專案旨在解決 Vibe Coding 開發模式下，因高頻率調用模型 API 導致的 Token 消耗難以追蹤、成本不可控的問題。透過建立自動化監控、預算閘道與成本預估模型，實現「高效開發、精準預算」。

## 1. 核心目標
*   **即時監控：** 整合 Helicone/LiteLLM，達成 100% 的 API 調用透明化。
*   **預算管控：** 設定硬性上限 (Hard Limits)，防止單日或單月費用爆表。
*   **成本預估：** 基於歷史數據，自動生成每月成本預測報表。

---

## 2. 技術方案規劃

### 方案 A：流量網關監控 (Gateway Observability) - **首選建議**
*   **工具：** Helicone.ai
*   **機制：** 將所有專案的 API Base 指向 Helicone Proxy。
*   **功能：** 
    *   自動解析 Input/Output Tokens。
    *   透過 `Helicone-Property-Project` 標籤區分不同專案開銷。
    *   支援快取 (Caching) 以減少重複開發造成的支出。

### 方案 B：預算閘道 (Budget Guardrail)
*   **工具：** LiteLLM Proxy
*   **機制：** 在本地或伺服器部署 LiteLLM，作為所有 LLM 請求的中轉站。
*   **功能：** 
    *   設定各個專案的 Token 或金額配額 (Quota)。
    *   當日消耗達 80% 時發送 Telegram 提醒。
    *   超過 100% 時自動暫斷服務。

### 方案 C：成本預估模型 (Estimation Framework)
*   **工具：** 自研 Python 腳本 + Supabase + Google Sheet
*   **機制：** 
    *   每日抓取監控 API 的消耗總量。
    *   使用「線性回歸」或「基準抽樣」算法預估月底結算金額。

---

## 3. 執行階段 (Execution Phases)

### Phase 1: 基礎設施建立 (Week 1)
*   [ ] 註冊並配置 Helicone 帳戶。
*   [ ] 建立 API Key 安全管理規範。
*   [ ] **Milestone:** 完成第一個專案的 Helicone 接入，能在 Dashboard 看到即時花費。

### Phase 2: 全專案標籤化與監控 (Week 2)
*   [ ] 盤點所有 Vibe Coding 工具（Claude Code, OpenClaw, Cursor 等）。
*   [ ] 統一更換 API 端點，並強制要求加入專案標籤 Header。
*   [ ] **Milestone:** 達成「分專案成本佔比圖」的可視化。

### Phase 3: 預算警戒與自動化通知 (Week 3)
*   [ ] 開發 Telegram Bot 通知模組。
*   [ ] 串接 Supabase 紀錄每日消耗總額。
*   [ ] **Milestone:** 每日晚間 10 點收到當日消耗與月底預估報告。

### Phase 4: 成本優化與快取策略 (Week 4)
*   [ ] 針對高頻重複請求開啟快取機制。
*   [ ] 評估使用小模型 (如 Gemini Flash) 替代昂貴模型做初級開發的成本效益。
*   [ ] **Milestone:** 達成在不影響開發速度下，降低 30% 以上的非必要支出。

---

## 4. 預算公式參考
`每月預估 = (前7日平均消耗 * 剩餘天數) * 1.2 (開發高峰緩衝)`

---

## 5. 聯絡與貢獻
*   **專案維護：** 米爸 & 小糰子 🍡
*   **最後更新：** 2026-02-13
