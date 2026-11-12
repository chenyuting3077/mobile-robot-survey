# VLN 與導航基礎模型

## 在解決的問題

- 語言對應到空間：把「走到廚房冰箱旁」對到畫面與地圖上的位置。
- 長程、部分可觀測：指令長、環境沒看過，需要記憶與探索。
- sim-to-real：benchmark 多在 Habitat 模擬，實機成功率落差大。
- 推論延遲：數 B 參數的 VLM 難以機上即時跑，近期多改成「慢 VLM 推理 + 快控制層」。
- 跨機體：同一模型用在輪式、四足、人形。

## 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-11 | [SPAN-Nav](https://arxiv.org/abs/2603.09163) | PKU / BAAI | 以 occupancy 預測學空間先驗並壓成單一 spatial token，類 CoT 方式注入動作推理的端到端導航基礎模型 | 420 萬筆室內外 occupancy 標註；三個導航 benchmark SOTA（作者自報）；實機驗證 | 未公開 | CoRL 2026 |
| 2026-11 | [PIGEON](https://arxiv.org/abs/2511.13207) | PKU / BAAI / CASIA | VLM 只在稀疏「興趣點」（frontier、疑似目標、樓梯、樓層摘要）間選擇，低階規劃器執行；決策可驗證，用 RLVR 微調本地 VLM | Habitat ObjectNav 零樣本 SOTA（作者自報）；改提示即可轉 Active EQA；實機部署 | 未公開 | CoRL 2026 |
| 2026-11 | [GTA](https://arxiv.org/abs/2602.15400) · [專案頁](https://zeruili22.github.io/GTA/) | Univ. of Adelaide / Manchester / Zhejiang Univ. / A*STAR | 空間狀態估計與 MLLM 規劃分離：累積幾何加導航歷史的度量世界表示供 MLLM 選 waypoint，反事實分支推理在觀測不符時修正決策 | R2R-CE val-unseen SR 48.8%、RxR-CE 子集 46.2%；輪式、四足、無人機實機 | [GitHub](https://github.com/zeruili22/GTA) | CoRL 2026 |
| 2026-11 | [CoFL-S](https://arxiv.org/abs/2607.02222) | Univ. of Tokyo | 預測局部可視扇區上的語言條件 flow field 再 rollout 成連續軌跡，取代離散前進／轉向動作；VLN-CE episode 轉成逐幀子指令監督 | 自建連續時間 Habitat benchmark 各規劃頻率皆勝過基線（作者自報）；零樣本實機閉環 | [GitHub](https://github.com/ut-dragon-lab/CoFL) | CoRL 2026 |
| 2026-10 | [Action Self-Distillation](https://arxiv.org/abs/2610.17593) · [專案頁](https://asd-nav.github.io) | Princeton | 同一個開源 VLM 當老師與學生：老師看特權軌跡回推目標與推理，學生只用機載觀測學預測軌跡與語言推理，不需人工標註 | 13 個實機任務：室內成功率比最強基線高 30%、多階段任務高 30%、室外 95% | 未公開 | CoRL 2026 |
| 2026-10 | [AVALON](https://arxiv.org/abs/2610.21586) | HKU | 只需平面圖與地點線索，以人給的分層拓撲記憶做節點驗證式導航，不建全域 SLAM 圖；人與機器人共同更新記憶 | Unitree Go2 實機 12.81 m 任務 46.4 s（5/5），比 DimOS-Go2 少 40.9% 時間 | 未公開 | arXiv |
| 2026-09 | [AgentVLN](https://arxiv.org/abs/2603.17670) | NUAA | 把 VLM 當大腦、感知與規劃拆成技能庫，3D waypoint 投影回影像當視覺提示，可部署在邊緣平台 |  | [GitHub](https://github.com/Allenxinn/AgentVLN) | ECCV 2026 |
| 2026-09 | [MM-Nav](https://arxiv.org/abs/2510.03142) · [專案頁](https://pku-epic.github.io/MM-Nav-Web/) | PKU / Galbot | 360° 多視角 VLA，向三個分別擅長抵達、穿窄、閃避的 RL 專家學，依各能力表現動態調訓練比例；有實機實驗 |  | 未公開 | ECCV 2026 |
| 2026-07 | [Robostral Navigate](https://arxiv.org/abs/2607.20785) · [專案頁](https://mistral.ai/news/robostral-navigate) | Mistral AI | 8B VLM 只用單眼 RGB，在畫面上指出下一個目標點；目標不在視野時輸出局部座標位移 | R2R-CE val-unseen SR 76.6%；online RL +3.2% | 未公開 | arXiv、Mistral 官網 |
| 2026-07 | [ABot-N1](https://arxiv.org/abs/2607.10383) · [專案頁](https://amap-cvlab.github.io/ABot-Navigation/ABot-N1/) | Alibaba AMAP | 慢 VLM 推理出影像錨點，快模組轉成連續 waypoint；同一架構做 point/object/POI/指令/跟人五種任務 | 室內 95.4%、室外 92.9% SR；POI 抵達 77.3% | [GitHub](https://github.com/amap-cvlab/ABot-Navigation) | arXiv |
| 2026-05 | [OmniNavBench](https://arxiv.org/abs/2605.09441) | SJTU / Anyverse Dynamics | 跨技能與跨機體的統一導航 benchmark：同一 episode 串接 6 類子任務，含人形、四足、輪式 | 170 環境、1779 條人工遙控專家軌跡 | [GitHub](https://github.com/AutoLab-SAI-SJTU/OmniNavBench) | RSS 2026 |
| 2026-04 | [Robot Navigation via Foundation Language Models: A Review](https://dl.acm.org/doi/10.1145/3802539) | ECNU / HIT 等 | ACM CSUR 綜述 |  | 未公開 | ACM Computing Surveys 2026 |
| 2026-03 | [LCVN](https://arxiv.org/abs/2603.26741) | University of Washington / NUS / Clemson | 語言條件的導航世界模型，比較不同預測方式在陌生環境的泛化能力 |  | [GitHub](https://github.com/UWMILab/LCVN) | NeurIPS 2026 |
| 2026-03 | [OpenFrontier](https://arxiv.org/abs/2603.05377) · [專案頁](https://boysun045.github.io/OpenFrontier-Project/) | ETH Zurich / Microsoft / Bonn | 把導航視為稀疏子目標辨識，用視覺 frontier 當語意錨點，不需稠密語意地圖與任務訓練；有實機部署 |  | [GitHub](https://github.com/cvg/OpenFrontier) | RSS 2026 |
| 2026-02 | [ABot-N0](https://arxiv.org/abs/2602.11598) · [專案頁](https://amap-cvlab.github.io/ABot-Navigation/ABot-N0/) | AMAP CV Lab | 單一 VLA 涵蓋多種導航任務，並加上分層拓撲記憶的規劃系統，支援真實環境長程任務 | 1,690 萬條專家軌跡；7 個 benchmark 宣稱 SOTA | [GitHub](https://github.com/amap-cvlab/ABot-Navigation) | arXiv |
| 2026-02 | [AsyncVLA](https://arxiv.org/abs/2602.13476) | UC Berkeley / Toyota / Princeton | 語言模型與邊緣控制非同步運作，通訊延遲下仍能反應環境；有實機驗證 | 延遲最高 6 秒時成功率高 40% | [GitHub](https://github.com/NHirose/AsyncVLA) | CoRL 2026 |
| 2026-02 | [TIC-VLA](https://arxiv.org/abs/2602.02459) · [專案頁](https://ucla-mobility.github.io/TIC-VLA/) | UCLA | 把語言推理延遲納入控制迴路，推理延遲數秒仍能即時控制；有實機實驗與 DynaNav 模擬套件 |  | [GitHub](https://github.com/ucla-mobility/TIC-VLA) | ICML 2026 |
| 2026-02 | [LongNav-R1](https://arxiv.org/abs/2602.12351) | University of Michigan | 把導航改寫成 VLA 與環境的多輪對話，用線上多輪 RL 依不同 horizon 估優勢；有實機零微調驗證 | Qwen3-VL-2B 成功率 64.3% → 73.0%（4000 條 rollout） | [GitHub](https://github.com/UMich-CURLY/LongNav-R1) | RSS 2026 |
