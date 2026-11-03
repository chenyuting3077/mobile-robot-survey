# 移動操作感知（導航銜接、抓取、物件遞交）

## 在解決的問題

- 導航到操作的銜接：導航只需粗略位置，抓取需要精確得多的幾何；底盤停在哪裡（base placement）決定手臂搆不搆得到。
- 抓取位姿感知：對沒看過的物件與夾爪，從部分點雲生成無碰撞的 6-DoF 抓取，且要容忍深度雜訊。
- 多相機分工：機身或頭部相機看全局，腕部相機看接觸區，目標要能在相機間接手、被遮擋時不跟丟。
- 共用場景表示：同一份地圖要同時回答「在哪裡」與「怎麼操作」，並隨物件被移動、門被打開而更新。

## 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-10 | [FOUND-IT++](https://arxiv.org/abs/2610.23622) | MIT SPARK / Samsung Research America | 基礎模型驅動的階層場景圖在 Jetson Thor 上機，只用單目未校正 RGB（VGGT-Ω 建圖、SAM 3 分割）跑完找物、抓取與歸位 | 10 次任務：導航到物件 100%（76/76）、抓取 50%（9/18）、放置 94%（17/18）；抓取失敗歸因於缺主動深度回饋與策略過於簡單 | [GitHub](https://github.com/MIT-SPARK/FOUND-IT) | arXiv |
| 2026-09 | [REAL](https://arxiv.org/abs/2607.13653) | SJTU / Shanghai AI Lab 等 | 移除模擬器的 oracle 感知 API、只留實體可得的場景先驗，加上模擬使用者，訓練會探索與追問的移動操作 agent | 實機 60 episodes 端到端 78.3%；REAL-Bench 互動任務 56.9% | [GitHub](https://github.com/InternRobotics/REAL) | ECCV 2026 |
| 2026-07 | [HoMMI](https://arxiv.org/abs/2603.03243) · [專案頁](https://hommi-robot.github.io) | Stanford / Toyota Research Institute | 頭部與腕部相機合用，加主動頸部補視野，從人類示範學全身移動操作；消融實驗量化單一視角的損失 | 實機 Delivery：完整 85%、只用腕部 15%、只用頭部 5%；Laundry 90%；Tablescape 80% | [GitHub](https://github.com/xxm19/hommi) | RSS 2026 |
| 2025-11 | [Affordance-Guided Base Placement](https://arxiv.org/abs/2511.06240) | NTU / NYCU | 零樣本從 affordance 由粗到細探索底盤停靠位置，不只對準物件中心 | Isaac Sim TIAGo++ 五項任務 85%，基線最高 61%；未做實機 | 未公開 | AAAI 2026 |
| 2024-10 | [DovSG](https://arxiv.org/abs/2410.11989) · [專案頁](https://bjhyzj.github.io/dovsg-web) | Beihang / CityU HK 等 | 開放詞彙場景圖在每個子任務後局部更新，取代靜態地圖，支援長期語言指令移動操作 | 與靜態場景方法比，長期任務成功率高 30%、更新最快 27 倍、記憶體少 13 倍 | [GitHub](https://github.com/BJHYZJ/DovSG) | RA-L 2025 |
