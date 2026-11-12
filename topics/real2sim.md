# 模擬與 Real2Sim

## 在解決的問題

- 視覺擬真：模擬器畫面和真實影像有落差，改用 NeRF／3DGS 重建真實場景來渲染。
- 物理可用：重建的場景要有碰撞網格、關節、材質，才能互動與訓練。
- 低成本擷取：手機或手持相機掃描就能建。
- 在數位分身裡訓練或評估策略，再部署回實機（real-to-sim-to-real）。
- 另一路線是生成式 world model（如 Cosmos）直接產生訓練資料。

## 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-11 | [VisionSIM](https://arxiv.org/abs/2611.08368) | UW–Madison / Portland State / CMU | 模擬感測器的原始物理量測過程，重現 LiDAR pileup、iToF 相位纏繞、事件相機不應期、熱像儀歷史相依等失效模式 | 釋出含同步原始量測與標註的大型室內資料集 | [GitHub](https://github.com/wision-lab/visionsim) | CoRL 2026 |
| 2026-11 | [RoboSnap](https://arxiv.org/abs/2607.06699) · [專案頁](https://robosnap.github.io) | Shanghai AI Lab / Tsinghua / Zhejiang Univ. / SJTU | 單張 RGB 轉可模擬場景：互動區前景做碰撞感知資產，背景用 3DGS 保留新視角外觀 | DROID 場景軌跡重播可靠；新資料集 DROID-Sim（564 場景）；模擬與實機評估結果相關 | [GitHub](https://github.com/robosnap/robosnap) | CoRL 2026 |
| 2026-11 | [NavVerse](https://arxiv.org/abs/2607.19695) | Univ. of Michigan / Tsinghua | 室內走到室外的連續導航 benchmark，透過可執行的機器人介面評估成功率、效率與安全 | 200 個場景、10,000 episodes；零樣本下 VLA 成功率最高、模組化方法最安全 | [GitHub](https://github.com/UMich-CURLY/NavVerse-Benchmark) | CoRL 2026 |
| 2026-11 | [Infinigen-Articulated](https://arxiv.org/abs/2505.10755) | Princeton / McGill / Cisco | 18 類可動物件的程序生成器，含物理參數並可匯出到常見機器人模擬器 | 生成資產可用於可動物件分割、RL 泛化與模仿學習 sim-to-real（作者自報） | [GitHub](https://github.com/princeton-vl/infinigen) | CoRL 2026 |
| 2026-11 | [Kamino](https://arxiv.org/abs/2603.16536) | Disney Research / NVIDIA | 原生支援運動學閉迴路與異質機體批次模擬的 GPU 剛體求解器，以 ADMM 解非線性互補問題，不近似成運動學樹 | 單 GPU 4,096 個平行環境，訓練含 6 個巢狀閉迴路的雙足行走策略 | [GitHub](https://github.com/newton-physics/newton) | CoRL 2026 |
| 2026-10 | [GRASE](https://arxiv.org/abs/2610.21498) | 西安交通大學、福州大學、Adobe、西湖大學 | 把影片當持續參照的 agent 流程：渲染結果與影像不符就回頭修正房間結構與物件擺放，而非一次到底 |  | 未公開 | arXiv |
| 2026-09 | [SPEAR](https://arxiv.org/abs/2607.06701) · [專案頁](https://mikeroberts3000.github.io/papers/spear) | Adobe / Intel Labs / Manycore / NVIDIA | Python 函式庫，可程式化控制任何 Unreal Engine 應用，並提供其他 UE 模擬器沒有的真值影像 | 開放超過 1.4 萬個 UE 函式 | [GitHub](https://github.com/spear-sim/spear) | ECCV 2026 |
| 2026-09 | [Habitat-GS](https://arxiv.org/abs/2604.12626) · [專案頁](https://zju3dv.github.io/habitat-gs/) | Zhejiang | 擴充 Habitat-Sim，以 3DGS 渲染場景並加入可驅動的高斯人體，用於訓練人感知導航 |  | [GitHub](https://github.com/zju3dv/habitat-gs) | ECCV 2026 |
| 2026-09 | [ReVeal](https://arxiv.org/abs/2609.23910) | Purdue / Samsung SDS | 考慮重建品質的 real-to-sim VLA 策略評估 |  | 未公開 | arXiv |
| 2026-06 | [ArtiTwinSplat](https://arxiv.org/abs/2606.24628) | ETH / Microsoft / Bonn | 手持 RGB-D 影片重建可互動數位分身（3DGS），輸出碰撞網格、門／抽屜關節、URDF，可直接匯入 Isaac Sim |  | 未公開 | arXiv |
| 2026-06 | [Robots Need More than VLA and World Models](https://arxiv.org/abs/2606.06556) | Motoniq.ai / Stanford / ETH 等 | 立場論文；整理 3DGS 模擬器訓練的導航策略可 zero-shot 轉移到實機（SOUS VIDE、SINGER、GRaD-Nav） |  | 未公開 | arXiv |
| 2026-04 | [GS-Playground](https://arxiv.org/abs/2604.25459) · [專案頁](https://gsplayground.github.io) | THU / Motphys / Dexmal / DISCOVER Robotics 等 | 高吞吐量寫實模擬器加自動 Real2Sim 流程，重建可直接模擬的場景，涵蓋行走、導航與操作 |  | [GitHub](https://github.com/discoverse-dev/gs_playground) | RSS 2026 |
| 2025-12 | [PolaRiS](https://arxiv.org/abs/2512.16881) · [專案頁](https://polaris-evals.github.io/) | UW / UC Berkeley / Stanford / TRI / Physical Intelligence 等 | 可擴展的 real-to-sim 通用策略評估 |  | [GitHub](https://github.com/arhanjain/polaris) | RSS 2026 |
| 2025-09 | [EmbodiedSplat](https://arxiv.org/abs/2509.17430) · [專案頁](https://gchhablani.github.io/embodied-splat) | Georgia Tech / TRI | 手機掃描建 3DGS 場景，在 Habitat-Sim 裡微調導航策略後部署回實機 |  | [GitHub](https://github.com/gchhablani/embodied-splat-v1) | ICCV 2025 |
