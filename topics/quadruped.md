# 四足

## 在解決的問題

- 感知不可靠時仍要穩（反光、草叢、高度圖雜訊）：融合外部感知與本體感知。
- sim-to-real：大規模平行模擬 + domain randomization + 特權教師蒸餾。
- 敏捷技能（跑酷、跳躍、越溝）與技能切換。
- 從「跟隨速度指令」走向「運動與導航一體」，直接走到目標。

## 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-11 | [Uni-Mo](https://arxiv.org/abs/2606.28237) | Alibaba AMAP | 不經動物動捕：LLM 提動作描述、影片擴散生成機器狗影片、提升成 3D 參考軌跡訓練追蹤策略，加身分一致性損失穩定生成 | 開源 7,488 段（18.5 小時）動作資料集；Go2 實機抽測 392 段成功率 96.7% | [GitHub](https://github.com/Amap-Robotics/Quad-Imaginarium) | CoRL 2026 |
| 2026-11 | [QWM](https://arxiv.org/abs/2604.08780) · [專案頁](https://modanesh.github.io/papers/qwm/) | Mila / McGill / ETH Zurich | 以尺度不變的形態特徵條件化單一生成式動力學模型，策略完全在 world model 想像中訓練 | 未見過的四足形態零樣本轉移，同樣形態資訊的 model-free 策略則退化（作者自報） | [GitHub](https://github.com/modanesh/QWM) | CoRL 2026 |
| 2026-11 | [LoComposition](https://arxiv.org/abs/2606.15896) · [專案頁](https://sites.google.com/view/locomposition) | TUM / Univ. of Tübingen / MPI-IS | 任務用獎勵、操作限制用約束、步態交給能量最小化、地形適應交給外感知，去掉所有步態先驗 | 地形通過率相當下運輸成本降 56%、限制違反降 96%；Go2 + LiDAR 高程圖零樣本實機 | 未公開 | CoRL 2026 |
| 2026-11 | [MorFiC](https://arxiv.org/abs/2603.14554) · [專案頁](https://prakharmishra27.github.io/MorFiC) | UMD / George Mason Univ. | 共享 critic 會平均不相容的跨機體價值目標；改用形態潛變量乘法調變 critic，單一機體加形態隨機化訓練 | 零樣本轉移 7 款機器人，AlienGo 1.98 m/s（加法式 PPO < 0.65 m/s）；訓練 2 小時；Go1、Go2 實機 | [GitHub](https://github.com/prakharmishra27/morfic-rl) | CoRL 2026 |
| 2026-10 | [SHOES](https://arxiv.org/abs/2610.16457) | Univ. of Tokyo / Tokyo Univ. of Agriculture and Technology | 凍結模擬訓練的策略，只在實機微調恆等初始化的輕量調變模組，適應穿鞋造成的足部形態改變；SafeBox 限制線上適應範圍 | 同預算下勝過 FiLM-only、Linear Adapter、residual RL；Go2 穿人鞋實機 | 未公開 | CoRL 2026 |
| 2026-10 | [End-to-End RL for Quadrupedal Jumping in Lunar Gravity](https://arxiv.org/abs/2610.29586) | ETH RSL | 多階段 RL 訓練單一端到端策略，只用任務可用的機載感測做指定點跳躍 | 模擬落點誤差小於機身尺寸；月球重力卸載下實機垂直跳 | 未公開 | arXiv |
| 2026-07 | [APT-RL: Agile perceptive multi-skill locomotion](https://arxiv.org/abs/2607.13579) · [專案頁](https://skillquadsr.github.io/) | KAIST 等 | 軌跡最佳化 8 分鐘產生 18 萬條動作先驗，再用 RL + 機載感知適應 3D 地形 | 單一策略過樓梯／欄／踏石／溝；瞬間最高 6 m/s | 未公開 | Science Robotics 2026 |
| 2026-06 | [Perceptive Platform Adaptive Locomotion](https://arxiv.org/abs/2606.25179) | Oxford DRS | 感知只給 critic，感知有雜訊時比完全感知策略穩 |  | 未公開 | arXiv |
| 2026-06 | [GUIDE](https://arxiv.org/abs/2606.10832) · [專案頁](https://guide-navigation.github.io/) | Zhejiang / TeleAI / Oxford 等 | 端到端腿式導航 |  | 未公開 | arXiv |
| 2026-04 | [HiPAN](https://arxiv.org/abs/2604.26504) · [專案頁](https://sgvr.kaist.ac.kr/~Jeil/project_page_HiPAN/) | KAIST | 非結構 3D 環境的姿態自適應分層導航 |  | 未公開 | RA-L 2026 |
