# 語意地圖與場景圖

## 在解決的問題

- 開放詞彙：不限定類別，能用任意語言查物件與區域。
- 可擴展：稠密特徵地圖太大，改用物件／房間／樓層的階層場景圖壓縮。
- 即時、增量：邊走邊建，並處理場景變動。
- 當成 LLM／VLM 規劃的介面。

## 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-11 | [MoMa-SG](https://arxiv.org/abs/2602.16356) · [專案頁](https://momasg.cs.uni-freiburg.de) | Univ. of Freiburg / ETH Zurich / Univ. of Bonn | 從含開關動作的 RGB-D 序列建語意加運動學 3D 場景圖：統一 twist 估計一次求轉動與平移關節，並推論容器與內含物件 | 新資料集 Arti4D-Semantic（62 序列、600 次互動）；四足與移動操作機實機 | [GitHub](https://github.com/robot-learning-freiburg/MoMa-SG) | CoRL 2026 |
| 2026-11 | [Language as a Sensor](https://arxiv.org/abs/2606.08666) · [專案頁](https://aryan-naveen.github.io/language-as-a-sensor/) | MIT SPARK / MIT CSAIL | 把話語與場景圖情境轉成多峰空間分布（權重表指涉歧義、協方差表位置不確定），當隨機觀測與機載感知融合進信念地圖 | VLA-3D 與實機上唯一校準良好的語言預測器；真實目標機率質量比最強基礎模型基線多約 70% | [GitHub](https://github.com/MIT-SPARK/Language-As-A-Sensor) | CoRL 2026 |
| 2026-10 | [CoSMO](https://arxiv.org/abs/2610.18321) · [專案頁](https://yangming911.github.io/cosmo-page/) | SJTU / Shanghai Innovation Institute / Fudan | 在 VLM embedding 空間做線上 conformal 校準，詞彙擴增時不需重新縮放分數，輸出具覆蓋保證的語意集合與依類別膨脹的障礙物 | MP3D 語意碰撞比純幾何基線少 61.6%；四足實機長期覆蓋率 90.73%（目標 90%） | [GitHub](https://github.com/Yangming911/CoSMO) | CoRL 2026 |
| 2026-09 | [Functional-SLAM](https://arxiv.org/abs/2609.07497) | Dalian Univ. of Technology / Tsinghua / ETH Zurich | 把功能場景圖當作線上 SLAM 狀態遞迴維護，並用功能拓撲輔助外觀重複場景的回環 | 比離線建圖快很多且準確度相當；功能拓撲回環提升位姿精度（作者自報） | [GitHub](https://github.com/Hbelief1998/Functional-SLAM-CoRL_2026) | CoRL 2026 |
| 2026-10 | [OASIS](https://arxiv.org/abs/2610.30589) · [專案頁](https://starry-curry-30.github.io/oasis-project) | Beihang Univ. | 以少量穩定語意錨點節點建立線上地圖，每個節點整合語意描述、視覺特徵與幾何，支援開放詞彙檢索並在場景變動後重新定位被移動的物件 |  | [GitHub](https://github.com/starry-curry-30/OASIS) | ACM MM 2026 |
| 2026-10 | [AOV-GS](https://arxiv.org/abs/2610.29374) | MIPT / AIRI | 主動 3D Gaussian 建圖：以 SAM 實例的 CLIP 嵌入新穎度重排候選視角，不需人工標註遮罩 | 同樣 SAM-CLIP 下語言場 mIoU 比純幾何探索高 1.3 pp（Replica 34.6%）、1.8 pp（Matterport3D 23.1%） | [GitHub](https://github.com/OptimusFaber/AOV-GS) | AIST 2026 |
| 2026-10 | [Industrial ReMEmbR](https://arxiv.org/abs/2610.28624) | Idealworks / NVIDIA | 把 ReMEmbR 擴成多機器人共用的時空記憶：機上只上傳嵌入與視覺 token，描述改為查詢時才生成，並把人像遮掉 | NaVQA 首次解析失敗率 20.7% → 13.8%；快取 token 解碼 450 次與原模型輸出一致 | 未公開 | arXiv |
| 2026-09 | [PUF](https://arxiv.org/abs/2607.07170) | Leibniz Hannover / IIT / Bath | 線上 3D 場景圖不再確定性融合，把節點關聯改成機率似然，不需訓練即可外掛到既有方法 |  | [GitHub](https://github.com/yyyyangyi/PUF) | ECCV 2026 |
| 2026-09 | [NoPA](https://arxiv.org/abs/2607.00529) · [專案頁](https://qixun1.github.io/projects/nopa/) | NUS | 線上場景圖的物件從單一高斯改為固定數量粒子，保留幾何細節，並在高相似物件間傳播關係 |  | [GitHub](https://github.com/qixun1/nopa) | ECCV 2026 |
| 2026-09 | [OP3DSG](https://arxiv.org/abs/2606.29786) · [專案頁](https://k2room.github.io/OP3DSG/) | GIST | 開放詞彙場景圖加入物件零件與 affordance 層，並提出 UniGraph3D benchmark；有實際機器人任務驗證 |  | [GitHub](https://github.com/AutoCompSysLab/OP3DSG) | ECCV 2026 |
| 2026-05 | [LEXI-SG](https://arxiv.org/abs/2605.13741) · [專案頁](https://ori-drs.github.io/lexisg-web/) | Oxford | 只用單眼 RGB 建開放詞彙 3D 場景圖，以房間為單位 feed-forward 重建 | 評估在 HM3D 與自錄辦公室序列，未做實機導航 | 未公開 | RA-L 2026 |
