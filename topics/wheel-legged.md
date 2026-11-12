# 輪足（雙足輪、四足輪）

## 在解決的問題

- 混合運動：何時滾、何時走、何時跨越，以及模式切換。
- 高速下的感知延遲：建圖更新跟不上速度（Lee et al. 2024 指出這限制了自主時的速度）。
- 硬體負載：輪驅動改變關節受力（Go2-W 髖關節過熱）。
- 雙足輪的平衡與越障；研究多停在運動控制，經典論文少。

## 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-11 | [S2M-Trek](https://arxiv.org/abs/2606.01332) | HUST / HIT | 輪足四足背上無圍欄運多顆自由滾動球：Per-Frame Deep Sets 先在每個歷史幀內做排列不變池化再讀時間，最後蒸餾成觸覺接觸圖策略 | 模擬五球階段 5 個 seed 皆 100% 無掉落 | [GitHub](https://github.com/Drgon-li/S2M-Trek) | CoRL 2026 |
| 2026-10 | [RAIWAY](https://arxiv.org/abs/2610.33172) | KAIST | 20 吋大輪雙足輪機器人；在模擬中把多接觸事件蒸餾成潛變量，部署時只用本體感測推估，不需接觸感測 | 實機通過陡坡、碎石、釘面、岩地，與最高 15 cm 階高的戶外階梯 | 未公開 | RA-L 2026 |
| 2026-02 | [Sparse MoE multi-mode locomotion](https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2026.1788395/full) | Beijing Institute of Technology | 雙足輪；稀疏 MoE RL，在滾動與越障間自動切換 |  | 未公開 | Frontiers in Robotics and AI 2026 |
