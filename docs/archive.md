<!-- 本檔由 scripts/build_readme.py 產生，請改 topics/、data/ 後重跑 -->

# 封存區

從重要論文移出但保留備查，規則見 [README](../README.md#怎樣算重要論文)，共 185 篇。

## VLN 與導航基礎模型：新興滿兩年未達門檻

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 新興 | 獲獎 | 2024 | [MiniVLN](https://arxiv.org/abs/2409.18800) | CASIA | 兩階段漸進式知識蒸餾，小模型保有 VLN 表現以利部署 | ICRA 2025<br>入圍 Best Conference Paper | 10 | 未公開 |
| 新興 | 獲獎 | 2023 | [Dynamic Navigation Goal from Dialogue](https://doi.org/10.1109/IROS55552.2023.10342509) | Shanghai Inst. of Tech. / Tsinghua 等 | 從自然語言對話中抽取會移動的目標（如人）的位置作為導航目標 | IROS 2023<br>🏆 Best Paper on Cognitive Robotics | 7 | 未公開 |

## VLN 與導航基礎模型：超過主題上限

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 主流 | 引用、Star | 2025 | [VLN-R1](https://arxiv.org/abs/2506.17221) · [專案頁](https://vlnr1.github.io) | Shanghai AI Lab / HKU | LVLM 以 GRPO 強化微調直接輸出連續導航動作 | arXiv | 84 | [547](https://github.com/Qi-Zhangyang/GPT4Scene-and-VLN-R1) |
| 主流 | 引用 | 2025 | [NavFoM](https://arxiv.org/abs/2509.12129) · [專案頁](https://pku-epic.github.io/NavFoM-Web/) | PKU / Galbot / USTC 等 | 跨載具跨任務導航基礎模型，800 萬筆多機種資料訓練 | ICLR 2026 | 116 | 未公開 |
| 主流 | 引用 | 2025 | [MTU3D](https://arxiv.org/abs/2507.04047) · [專案頁](https://mtu3d.github.io) | Tsinghua / BIGAI / BIT 等 | 3D 視覺定位與主動探索合一，支援多種目標模態 | ICCV 2025 | 97 | [276](https://github.com/MTU3D/MTU3D) |
| 主流 | 引用 | 2024 | [Uni-NaVid](https://arxiv.org/abs/2412.06224) · [專案頁](https://pku-epic.github.io/Uni-NaVid/) | PKU | 一個 VLM 統一 VLN、物件導航、問答、跟人等導航任務 | RSS 2025 | 244 | [361](https://github.com/jzhzhang/Uni-NaVid) |
| 主流 | 引用 | 2025 | [ApexNav](https://arxiv.org/abs/2504.14478) · [專案頁](https://robotics-star.com/ApexNav) | HKUST(GZ) / SUSTech | 依語意線索強弱切換探索策略，目標中心融合抗誤檢 | RA-L 2025 | 82 | [476](https://github.com/SYSU-STAR/ApexNav) |
| 主流 | 引用、獲獎 | 2025 | [WMNav](https://arxiv.org/abs/2503.02247) · [專案頁](https://b0b8k1ng.github.io/WMNav/) | CASIA / Wuhan Univ. / UTS | VLM 當世界模型預測決策結果並回饋策略 | IROS 2025<br>oral | 77 | [184](https://github.com/B0B8K1ng/WMNavigation) |
| 主流 | 引用、機構 | 2025 | [OmniVLA](https://arxiv.org/abs/2509.19480) · [專案頁](https://omnivla-nav.github.io/) | UC Berkeley / Toyota / Princeton | 語言、座標、影像多種目標模態共用的導航 VLA | ICRA 2026 | 65 | [365](https://github.com/NHirose/OmniVLA) |
| 主流 | 引用 | 2025 | [OmniNav](https://arxiv.org/abs/2509.25687) · [專案頁](https://astra-amap.github.io/omninav.github.io/) | Alibaba / PKU | 單一架構統一指令、物件、點目標導航與探索 | ICLR 2026 | 66 | [241](https://github.com/amap-cvlab/OmniNav) |
| 主流 | 引用 | 2024 | [NavGPT-2](https://arxiv.org/abs/2407.12366) | Adelaide / Adobe / UNC 等 | 凍結 LLM 的 VLM 特徵接拓撲圖策略，保留可解釋推理 | ECCV 2024 | 157 | [258](https://github.com/GengzeZhou/NavGPT-2) |
| 主流 | 引用 | 2024 | [MapGPT](https://arxiv.org/abs/2401.07314) · [專案頁](https://chen-judge.github.io/MapGPT/) | HKU / SYSU / Meituan | 線上拓撲地圖轉成提示讓 GPT 做全域路徑規劃 | ACL 2024 | 176 | [138](https://github.com/chen-judge/MapGPT) |
| 主流 | 引用 | 2024 | [NavCoT](https://arxiv.org/abs/2403.07376) | SYSU / Huawei Noah's Ark | LLM 自我引導解耦推理（想像、篩選、預測）並參數高效微調 | TPAMI 2025 | 155 | [144](https://github.com/expectorlin/NavCoT) |
| 主流 | 引用 | 2023 | [ESC](https://arxiv.org/abs/2301.13166) | UC Santa Cruz / Samsung Research | LLM 常識轉成軟性邏輯約束引導 frontier 探索 | ICML 2023 | 306 | 未公開 |
| 主流 | 引用 | 2023 | [NaviLLM](https://arxiv.org/abs/2312.02010) | CUHK / Shanghai AI Lab | schema 化提示讓單一 LLM 統一多種導航任務 | CVPR 2024 | 228 | [240](https://github.com/zd11024/NaviLLM) |
| 主流 | 引用 | 2024 | [LH-VLN](https://arxiv.org/abs/2412.09082) · [專案頁](https://hcplab-sysu.github.io/LH-VLN/) | SYSU | 多階段長程 VLN 任務，含自動資料生成平台與基準 | CVPR 2025 | 111 | [271](https://github.com/HCPLab-SYSU/LH-VLN) |
| 主流 | 引用 | 2024 | [OpenFMNav](https://arxiv.org/abs/2402.10670) · [專案頁](https://yuxuank.com/OpenFMNav/) | PKU / Notre Dame | LLM 解析自由指令加 VLM 建語意地圖做開放集物件導航 | NAACL 2024 Findings | 138 | [64](https://github.com/yxKryptonite/OpenFMNav) |
| 主流 | 引用 | 2024 | [Open-Nav](https://arxiv.org/abs/2409.18794) · [專案頁](https://sites.google.com/view/opennav) | Adelaide / SCUT | 開源 LLM 搭配時空 CoT 做連續環境零樣本 VLN | ICRA 2025 | 109 | [187](https://github.com/YanyuanQiao/Open-Nav) |
| 主流 | 引用 | 2025 | [VLN-PE](https://arxiv.org/abs/2507.13019) · [專案頁](https://crystalsixone.github.io/vln_pe.github.io/) | Tongji / Shanghai AI Lab / SJTU | 支援人形、四足、輪式的物理真實 VLN 平台與評測 | ICCV 2025 | 51 | 未公開 |
| 主流 | 引用 | 2025 | [OctoNav](https://arxiv.org/abs/2506.09839) · [專案頁](https://buaa-colalab.github.io/OctoNav) | Beihang / NUS / PKU 等 | 多模態多能力自由指令基準，加先思考再行動的 R1 模型 | CVPR 2026 | 45 | [78](https://github.com/buaa-colalab/OctoNav-R1) |
| 主流 | 引用 | 2023 | [GridMM](https://arxiv.org/abs/2307.12907) | ICT-CAS / UCAS | 動態成長的俯視網格記憶地圖結構化已訪環境 | ICCV 2023 | 210 | [106](https://github.com/MrZihan/GridMM) |
| 主流 | 引用 | 2024 | [VER](https://arxiv.org/abs/2403.14158) | Zhejiang | 多視角 2D 特徵聚合成 3D 體素表示環境 | CVPR 2024 | 101 | [143](https://github.com/DefaultRui/VLN-VER) |
| 主流 | 引用 | 2025 | [SmartWay](https://arxiv.org/abs/2503.10069) · [專案頁](https://sxyxs.github.io/smartway/) | Adelaide | 強化路徑點預測器加可回溯的 MLLM 導航器 | IROS 2025 | 45 | [20](https://github.com/sxyxs/SmartWay-Code) |
| 主流 | 引用 | 2024 | [VoroNav](https://arxiv.org/abs/2401.02695) · [專案頁](https://voro-nav.github.io) | PKU / Shanghai AI Lab / HKU | 簡化 Voronoi 圖萃取探索路徑節點交給 LLM 決策 | ICML 2024 | 123 | 未公開 |
| 主流 | 引用、獲獎 | 2025 | [Dynam3D](https://arxiv.org/abs/2505.11383) | NUS | 動態分層 3D token 當 VLM 輸入，隨環境更新 | NeurIPS 2025<br>oral | 38 | [95](https://github.com/MrZihan/Dynam3D) |
| 主流 | 引用 | 2024 | [AO-Planner](https://arxiv.org/abs/2407.05890) · [專案頁](https://chen-judge.github.io/AO-Planner/) | HKU / SYSU / Meituan | VLM 預測可行走路徑點，補上連續 VLN 底層控制 | AAAI 2025 | 107 | [48](https://github.com/chen-judge/AO-Planner) |
| 主流 | 引用 | 2024 | [HNR](https://arxiv.org/abs/2404.01943) | ICT-CAS / UCAS | 神經輻射表示預測候選點未來特徵做前瞻探索 | CVPR 2024 | 96 | [110](https://github.com/MrZihan/HNR-VLN) |
| 主流 | 引用、獲獎 | 2024 | [PoliFormer](https://arxiv.org/abs/2406.20083) · [專案頁](https://poliformer.allen.ai) | AI2 | 大規模 RL 訓練 Transformer 策略，RGB 直接轉實機 | CoRL 2024<br>🏆 Outstanding Paper | 90 | [106](https://github.com/allenai/PoliFormer) |
| 主流 | 引用 | 2024 | [GOAT (causal VLN)](https://arxiv.org/abs/2404.10241) | Tongji | 因果推論去除視覺、語言、歷史中的資料偏差 | CVPR 2024 | 89 | [104](https://github.com/CrystalSixone/VLN-GOAT) |
| 主流 | 引用 | 2023 | [PixNav](https://arxiv.org/abs/2309.10309) · [專案頁](https://sites.google.com/view/pixnav/) | Southeast Univ. / PKU / Shanghai AI Lab | 以像素為目標的導航技能銜接基礎模型與底層移動 | ICRA 2024 | 156 | [139](https://github.com/wzcai99/Pixel-Navigator) |
| 主流 | 引用 | 2024 | [Mobility VLA](https://arxiv.org/abs/2407.07775) | Google DeepMind | 長脈絡 VLM 看導覽影片建拓撲圖，再照多模態指令導航 | CoRL 2024 | 103 | 未公開 |
| 主流 | 引用 | 2021 | [EmbCLIP](https://arxiv.org/abs/2111.09888) | AI2 | 只換 CLIP 視覺骨幹不加任務設計就超越多項導航基線 | CVPR 2022 | 307 | [131](https://github.com/allenai/embodied-clip) |
| 主流 | 引用 | 2025 | [BeliefMapNav](https://arxiv.org/abs/2506.06487) | SJTU / UMich | 3D 體素信念地圖估計目標分布，結合序列路徑規劃 | NeurIPS 2025 | 35 | [51](https://github.com/ZiboKNOW/BeliefMapNav) |
| 主流 | 引用 | 2023 | [LGX](https://arxiv.org/abs/2303.03480) | UMD | LLM 序列決策加開放詞彙偵測找語言描述的目標物 | RA-L 2024 | 168 | [72](https://github.com/vdorbala/LGX) |
| 主流 | 引用 | 2025 | [OpenIN](https://arxiv.org/abs/2501.04279) · [專案頁](https://openin-nav.github.io) | BIT | 載體關係場景圖追蹤會移動的物件實例 | RA-L 2025 | 34 | 未公開 |
| 主流 | 引用 | 2023 | [GOAT](https://arxiv.org/abs/2311.06430) | UIUC / CMU / Georgia Tech 等 | 多模態目標、終身記憶的通用導航系統，實機長時間部署 | RSS 2024 | 165 | 未公開 |
| 主流 | 引用 | 2025 | [MoRE](https://arxiv.org/abs/2503.08007) | Zhejiang / Westlake / Monash 等 | 多 LoRA 專家 VLA 搭配 RL 微調，用混合品質資料 | ICRA 2025 | 31 | 未公開 |
| 新興 | 獲獎 | 2025 | [SocialNav](https://arxiv.org/abs/2511.21135) · [專案頁](https://amap-eai.github.io/SocialNav/) | Amap Alibaba | 「大腦-動作」階層架構，以 700 萬筆 SocNav 資料訓練遵守社會規範的導航基礎模型 | CVPR 2026<br>入圍 Best Paper | 23 | [137](https://github.com/AMAP-EAI/SocialNav) |

## 局部導航與規劃（diffusion / world model / 探索）：新興滿兩年未達門檻

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 新興 | 獲獎 | 2023 | [Sequential Neural Barriers](https://arxiv.org/abs/2307.03015) | （論文未列單位） | 依序學習神經控制障壁函數，動態障礙物數量增加時仍能擴展且對分布漂移較穩 | IROS 2023<br>🏆 Best RoboCup Paper | 29 | 未公開 |
| 新興 | 獲獎 | 2024 | [Hiking Trail Navigation](https://arxiv.org/abs/2409.15671) | West Virginia University | 語意分割判斷步道、幾何分析判斷可通行，必要時可離開步道 | IROS 2025<br>入圍 Award Finalist | 4 | 未公開 |
| 新興 | 獲獎 | 2022 | [Confidence-based Nav under Occlusion](https://doi.org/10.1109/ICRA46639.2022.9812090) | KAIST | 感測器被髒污遮擋時，以信心度驅動 RL 主動探索確保可見度 | ICRA 2022<br>入圍 Outstanding Navigation Paper | 12 | 未公開 |

## 四足：新興滿兩年未達門檻

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 新興 | 獲獎 | 2024 | [Confined-Space Legged Locomotion](https://arxiv.org/abs/2403.00187) | ETH RSL | 以 3D 體素表示輸入 RL 策略，四足能調整姿態鑽過狹窄空間 | ICRA 2024<br>🏆 Best Paper in Service Robotics | 69 | 未公開 |
| 新興 | 獲獎 | 2023 | [Multi-IMU Proprioceptive Odometry](https://doi.org/10.1109/IROS55552.2023.10342061) | CMU | 在每條小腿加裝 IMU，以 EKF 融合做低漂移的腿式本體感覺里程計 | IROS 2023<br>入圍 Best Paper on Safety, Security, and Rescue Robotics | 43 | [82](https://github.com/ShuoYangRobotics/Multi-IMU-Proprioceptive-Odometry) |
| 新興 | 獲獎 | 2023 | [Resilient Legged Local Navigation](https://arxiv.org/abs/2310.03581) | ETH RSL | 把感知失效建模成看不見的障礙與坑洞，RL 局部導航策略學會靠本體感覺應變 | ICRA 2024<br>入圍 Best Paper in Cognitive Robotics | 53 | 未公開 |
| 新興 | 獲獎 | 2024 | [Quadruped Ladder Climbing](https://arxiv.org/abs/2409.17731) · [專案頁](https://sites.google.com/leggedrobotics.com/climbingladders) | ETH RSL | 特製鉤爪加上 RL 策略，四足實機可靠爬工業爬梯 | IROS 2025<br>入圍 Award Finalist | 25 | 未公開 |
| 新興 | 獲獎 | 2022 | [Quadruped Soccer Shooting](https://arxiv.org/abs/2208.01160) | UC Berkeley / Mila | 階層式 RL：高層規劃踢球軌跡、低層追蹤，四足實機精準把球踢向指定目標 | IROS 2022<br>入圍 Best RoboCup Paper | 91 | 未公開 |
| 新興 | 獲獎 | 2024 | [Leader Following Quadruped](https://arxiv.org/abs/2410.00572) | ETH RSL | 四足以視覺追蹤領隊者並同時避障，免手動遙控跟隨 | ICRA 2025<br>入圍 Best Conference Paper | 19 | 未公開 |
| 新興 | 獲獎 | 2023 | [Steep Planetary Terrain Locomotion](https://doi.org/10.1109/IROS55552.2023.10341665) | ETH Zurich | 針對行星陡坡與鬆軟地形的四足行走策略 | IROS 2023<br>入圍 Best Paper | 21 | 未公開 |
| 新興 | 獲獎 | 2022 | [Distributed DDPC Collaborative Legged](https://arxiv.org/abs/2211.06917) | Virginia Tech / Caltech | 以行為系統理論建模多台互相拘束的四足，分散式資料驅動預測控制協同行走 | ICRA 2023<br>🏆 Outstanding Paper | 36 | 未公開 |
| 新興 | 獲獎 | 2022 | [PI-ARS](https://arxiv.org/abs/2207.13224) · [專案頁](https://kuanghuei.github.io/piars) | Google Research | 以預測資訊表示壓縮視覺輸入，讓演化策略能訓練較大的視覺步行策略 | IROS 2022<br>入圍 Best Paper | 21 | 未公開 |
| 新興 | 獲獎 | 2022 | [Motion Primitive Graph](https://arxiv.org/abs/2209.07503) | Caltech | 在動作基元圖上規劃，依擾動即時切換步態基元，提升腿式機器人穩健性 | ICRA 2023<br>🏆 Outstanding Student Paper<br>🏆 Outstanding Locomotion Paper | 16 | 未公開 |
| 新興 | 獲獎 | 2021 | [Mini Cheetah Optimal Landing](https://arxiv.org/abs/2110.02799) | MIT / UMass Amherst | 不預設接觸序列，即時最佳化落地姿勢與反作用力，從各種墜落狀態恢復 | ICRA 2022<br>入圍 Outstanding Dynamics and Control Paper | 8 | 未公開 |

## 四足：超過主題上限

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 新興 | 獲獎 | 2021 | [Fast and Efficient Gait Transitions](https://arxiv.org/abs/2104.04644) · [專案頁](https://sites.google.com/view/fast-and-efficient) | University of Washington / Google | 高層策略以 ES 學步態選擇、低層 MPC 執行，只用能耗獎勵就自然長出隨速度切換步態 | CoRL 2021<br>入圍 Best Systems Paper | 141 | [91](https://github.com/yxyang/fast_and_efficient) |
| 新興 | 獲獎 | 2021 | [Robotic Guide Dog](https://arxiv.org/abs/2103.14300) | UC Berkeley | 四足以牽繩混合物理互動引導人通過狹窄雜亂空間，牽繩鬆緊納入規劃 | ICRA 2021<br>入圍 Best Paper in Service Robotics | 120 | 未公開 |

## 輪足（雙足輪、四足輪）：新興滿兩年未達門檻

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 新興 | 獲獎 | 2022 | [Track-leg / Wheel-leg TrajOpt](https://doi.org/10.1109/ICRA46639.2022.9812199) | Florida State | 具平滑解析導數的軌跡最佳化，讓履帶腿、輪腿機器人規劃翻越大型障礙 | ICRA 2022<br>🏆 Outstanding Locomotion Paper | 4 | 未公開 |

## SLAM 與定位：新興滿兩年未達門檻

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 新興 | 獲獎 | 2023 | [NGEL-SLAM](https://arxiv.org/abs/2311.09525) | Zhejiang | 特徵式追蹤加回環確保全域一致，多個神經隱式子地圖做低延遲稠密建圖 | ICRA 2024<br>🏆 Best Paper in Robot Vision | 40 | [69](https://github.com/YunxuanMao/NGEL_SLAM) |
| 新興 | 獲獎 | 2024 | [Censible](https://doi.org/10.1109/ICRA57147.2024.10611697) | Caltech / JPL | 行星車全域定位框架，取代人工比對軌道影像 | ICRA 2024<br>入圍 Best Conference Paper | 17 | 未公開 |
| 新興 | 獲獎 | 2023 | [MESA](https://arxiv.org/abs/2310.12320) | CMU | 在流形上的共識 ADMM 後端，多機器人非同步分散式最佳化 SLAM | ICRA 2024<br>入圍 Best Paper on Multi-Robot Systems | 20 | 未公開 |
| 新興 | 獲獎 | 2022 | [EDPLVO](https://doi.org/10.1109/ICRA46639.2022.9812133) | Meituan / UNC / CMU | 把共線約束有效納入直接法，點線並用的高效直接視覺里程計 | ICRA 2022<br>🏆 Outstanding Navigation Paper | 40 | 未公開 |
| 新興 | 獲獎 | 2024 | [Square-Root Filter VINS](https://doi.org/10.1109/ICRA57147.2024.10610916) | University of Delaware | 改用平方根共變異數濾波，在嵌入式裝置上更快且數值更穩 | ICRA 2024<br>入圍 Best Paper in Robot Vision | 10 | 未公開 |
| 新興 | 獲獎 | 2023 | [Semantic Object Map Localization](https://arxiv.org/abs/2303.04658) | MIT | 以物件語意地圖做跨視角配準，不依賴道路特徵，在非都市環境做全域定位與重定位 | IROS 2023<br>入圍 Best Paper on Safety, Security, and Rescue Robotics | 16 | 未公開 |
| 新興 | 獲獎 | 2023 | [iMODE](https://doi.org/10.1109/ICRA48891.2023.10161538) | Imperial | 以稀疏 SLAM 位姿與深度監督，即時從頭訓練單目稠密語意神經場 | ICRA 2023<br>🏆 Outstanding Navigation Paper | 16 | 未公開 |
| 新興 | 獲獎 | 2023 | [Cross-View Place Recognition](https://doi.org/10.1109/IROS55552.2023.10341898) | University of Maryland | 保留視覺、空間、幾何資訊的語意地點辨識，用於空地協同的跨視角跨模態定位 | IROS 2023<br>🏆 Best Paper on Agri-Robotics | 11 | 未公開 |
| 新興 | 獲獎 | 2021 | [Ground Encoding](https://arxiv.org/abs/2103.15317) | CMU | 把透地雷達訊號學成因子圖量測模型，不需事前地圖或 GPS 就能定位 | IROS 2021<br>入圍 Best Paper | 21 | 未公開 |
| 新興 | 獲獎 | 2022 | [Data-driven Event Feature Tracking](https://arxiv.org/abs/2211.12826) | UZH RPG | 第一個資料驅動的事件相機特徵追蹤器，有無影像幀都能用，自監督適應真實資料 | CVPR 2023、TPAMI 2025<br>入圍 Best Paper | 17 | 未公開 |
| 新興 | 獲獎 | 2021 | [Unsupervised LiDAR Features](https://arxiv.org/abs/2102.11261) | University of Toronto | 在高斯變分推論框架內非監督學習 LiDAR 特徵，與軌跡估計共用單一目標 | RA-L 2021<br>🏆 ICRA 2021 Best Student Paper | 16 | 未公開 |
| 新興 | 獲獎 | 2023 | [GMCR](https://arxiv.org/abs/2303.04032) | TUM / Glasgow / Radboud | 以圖式最大共識估計做點雲配準，在高離群比例下仍穩健 | ICRA 2023<br>入圍 Outstanding Sensors and Perception Paper | 7 | 未公開 |
| 新興 | 獲獎 | 2021 | [Interval-Based Visual-LiDAR Fusion](https://doi.org/10.1109/LRA.2021.3057572) | Leibniz University Hannover | 以區間分析保守建模 LiDAR 距離指派給影像特徵的不確定性 | RA-L 2021<br>🏆 ICRA 2021 Best Paper in Robot Vision | 12 | 未公開 |

## SLAM 與定位：超過主題上限

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 主流 | 引用、Star | 2022 | [NeRF-SLAM](https://arxiv.org/abs/2210.13641) | MIT SPARK | 稠密單目 SLAM 提供位姿與深度不確定度即時訓練 NeRF | IROS 2023 | 403 | [1,266](https://github.com/ToniRV/NeRF-SLAM) |
| 主流 | 引用、Star | 2024 | [DPV-SLAM](https://arxiv.org/abs/2408.01654) | Princeton | DPVO 加上迴環的單 GPU 低記憶體深度視覺 SLAM | ECCV 2024 | 116 | [1,146](https://github.com/princeton-vl/DPVO) |
| 主流 | 引用 | 2025 | [MegaLoc](https://arxiv.org/abs/2502.17237) | PoliTo / Focoos AI | 合併多資料集訓練的通用影像檢索定位模型 | CVPRW 2025 | 88 | [316](https://github.com/gmberton/MegaLoc) |
| 主流 | 引用、獲獎 | 2024 | [SLAM in Extreme Environments (SubT)](https://doi.org/10.1109/TRO.2023.3323938) | NASA JPL / CMU / ETH 等 | DARPA SubT 各隊 SLAM 系統與地下環境經驗總整理 | T-RO 2024 | 244 | 未公開 |
| 主流 | 引用、Star、獲獎 | 2024 | [PIN-SLAM](https://arxiv.org/abs/2401.09101) | Bonn | 點式隱式神經地圖可隨迴環彈性變形的 LiDAR SLAM | T-RO 2024 | 135 | [632](https://github.com/PRBonn/PIN_SLAM) |
| 主流 | 引用、Star | 2023 | [Swarm-SLAM](https://arxiv.org/abs/2301.06230) · [專案頁](https://lajoiepy.github.io/cslam_documentation/html/index.html) | Polytechnique Montréal | 稀疏去中心化的多機器人協作 SLAM | RA-L 2024 | 222 | [722](https://github.com/MISTLab/Swarm-SLAM) |
| 主流 | 引用、Star | 2024 | [GS-ICP SLAM](https://arxiv.org/abs/2403.12550) | SKKU | G-ICP 與 3DGS 共用 Gaussian 地圖的高速 SLAM | ECCV 2024 | 142 | [540](https://github.com/Lab-of-AI-and-Robotics/GS_ICP_SLAM) |
| 主流 | 引用、Star | 2021 | [PixLoc](https://arxiv.org/abs/2103.09213) · [專案頁](https://psarlin.com/pixloc/) | ETH / Chalmers / Microsoft 等 | 對齊多尺度深度特徵的場景無關相機定位 | CVPR 2021 | 364 | [805](https://github.com/cvg/pixloc) |
| 主流 | 引用 | 2023 | [GO-SLAM](https://arxiv.org/abs/2309.02436) · [專案頁](https://youmi-zym.github.io/projects/GO-SLAM/) | Bologna | 迴環與全域 BA 即時更新神經重建的稠密 SLAM | ICCV 2023 | 258 | [442](https://github.com/youmi-zym/GO-SLAM) |
| 主流 | 引用、Star、獲獎 | 2023 | [MAC (Maximal Cliques)](https://arxiv.org/abs/2305.10854) | Northwestern Polytechnical | 放寬最大團限制，從相容圖中挖出多個極大團產生位姿假設，點雲配準更穩 | CVPR 2023<br>入圍 Best Paper | 226 | [546](https://github.com/zhangxy0517/3D-Registration-with-Maximal-Cliques) |
| 主流 | 引用、Star、獲獎、機構 | 2024 | [Khronos](https://arxiv.org/abs/2402.13817) | MIT SPARK | 統一處理短期動態與長期變化的時空度量語意 SLAM | RSS 2024<br>入圍 Outstanding Systems Paper | 105 | [554](https://github.com/MIT-SPARK/Khronos) |
| 主流 | 引用、Star | 2024 | [iG-LIO](https://doi.org/10.1109/LRA.2024.3349915) | Zhejiang | 增量 GICP 緊耦合 LIO，兼顧速度與精度 | RA-L 2024 | 104 | [526](https://github.com/zijiechenrobotics/ig_lio) |
| 主流 | Star、獲獎 | 2024 | [MAC-VO](https://arxiv.org/abs/2409.09479) | CMU / SJTU | 學出度量感知的匹配不確定性，同時用來挑關鍵點與加權位姿圖殘差 | ICRA 2025<br>🏆 Best Conference Paper<br>🏆 Best Paper on Robot Perception | 36 | [948](https://github.com/MAC-VO/MAC-VO) |
| 主流 | 引用、獲獎 | 2023 | [NICER-SLAM](https://arxiv.org/abs/2302.03594) · [專案頁](https://nicer-slam.github.io) | ETH / MPI-IS / Lund 等 | 僅用 RGB 並以單目先驗監督的神經隱式稠密 SLAM | 3DV 2024<br>🏆 Best Paper Honorable Mention | 280 | [217](https://github.com/cvg/nicer-slam) |
| 主流 | 引用 | 2024 | [Splat-SLAM](https://arxiv.org/abs/2405.16544) | Google / ETH / Univ. of Amsterdam 等 | 全域優化追蹤並隨之變形 Gaussian 地圖的純 RGB SLAM | CVPRW 2025 | 124 | [364](https://github.com/google-research/Splat-SLAM) |
| 主流 | 引用 | 2024 | [LoopSplat](https://arxiv.org/abs/2408.10154) · [專案頁](https://loopsplat.github.io/) | Stanford / Univ. of Amsterdam / ETH | 直接配準 3DGS 子地圖做迴環的 Gaussian SLAM | 3DV 2025 | 116 | [402](https://github.com/GradientSpaces/LoopSplat) |
| 主流 | 引用、Star | 2025 | [KISS-SLAM](https://arxiv.org/abs/2503.12660) | Bonn / Sapienza | 延續 KISS-ICP 免調參、泛化強的 LiDAR SLAM 基線 | IROS 2025 | 33 | [546](https://github.com/PRBonn/kiss-slam) |
| 主流 | 引用、Star、獲獎、機構 | 2025 | [GS-LIVO](https://arxiv.org/abs/2501.08672) | HKUST / HKU MaRS / SJTU | 可在嵌入式即時運行的 LiDAR 慣性視覺 Gaussian 建圖 | T-RO 2025 | 33 | [507](https://github.com/HKUST-Aerial-Robotics/GS-LIVO) |
| 主流 | 引用、獲獎 | 2025 | [OKVIS2-X](https://arxiv.org/abs/2510.04612) | TUM | 可選配稠密深度、LiDAR 與 GNSS 的關鍵幀 VI-SLAM | T-RO 2025 | 33 | [430](https://github.com/ethz-mrl/OKVIS2-X) |
| 主流 | 引用 | 2021 | [PointDSC](https://arxiv.org/abs/2103.05465) | HKUST / CityU | 把空間一致性做成可學習的離群點剔除，提升特徵式點雲配準的穩健度 | CVPR 2021 | 405 | [274](https://github.com/XuyangBai/PointDSC) |
| 主流 | 引用、獲獎 | 2024 | [BTC](https://doi.org/10.1109/TRO.2024.3353076) | HKU MaRS | 二值 + 三角形組合描述子的 3D LiDAR 地點辨識 | T-RO 2024 | 87 | [374](https://github.com/hku-mars/btc_descriptor) |
| 主流 | 引用 | 2024 | [SelaVPR](https://arxiv.org/abs/2402.14505) | Tsinghua / Peng Cheng Lab / UCAS | 以輕量 adapter 做全域與局部調適的基礎模型 VPR | ICLR 2024 | 102 | [269](https://github.com/Lu-Feng/SelaVPR) |
| 主流 | 引用 | 2024 | [CricaVPR](https://arxiv.org/abs/2402.19231) | Tsinghua / Peng Cheng Lab / UCAS | 批次內跨影像注意力學習相關性感知的 VPR 表示 | CVPR 2024 | 115 | [173](https://github.com/Lu-Feng/CricaVPR) |
| 主流 | 引用 | 2025 | [Adaptive-LIO](https://arxiv.org/abs/2503.05077) | 未確認 | 依環境自適應分段與地圖解析度的 LiDAR 慣性里程計 | IoT-J 2025 | 37 | [271](https://github.com/chengwei0427/Adaptive-LIO) |
| 主流 | 引用 | 2024 | [BoQ](https://arxiv.org/abs/2405.07364) | Laval | 以一組可學習全域查詢聚合特徵的單階段 VPR | CVPR 2024 | 108 | [197](https://github.com/amaralibey/bag-of-queries) |
| 主流 | 引用、獲獎 | 2025 | [VINGS-Mono](https://arxiv.org/abs/2501.08286) · [專案頁](https://vings-mono.github.io/) | Fudan | 視覺慣性單目 Gaussian SLAM 擴展到公里級戶外 | T-RO 2025 | 32 | [305](https://github.com/Fudan-MAGIC-Lab/VINGS-Mono) |
| 主流 | 引用 | 2022 | [REGTR](https://arxiv.org/abs/2203.14517) | NUS | 用 transformer 直接輸出對應點，免最近鄰匹配與 RANSAC，端到端點雲配準 | CVPR 2022 | 317 | [273](https://github.com/yewzijian/RegTR) |
| 主流 | 引用 | 2025 | [Ground-Fusion++](https://arxiv.org/abs/2507.08364) | Chongqing / Nankai / ZJUT 等 | GNSS、RGB-D、LiDAR、IMU、輪速的模組化融合 | IROS 2025 | 34 | [230](https://github.com/sjtuyinjie/Ground-Fusion2) |
| 主流 | 引用 | 2025 | [OpenGS-SLAM (outdoor)](https://arxiv.org/abs/2502.15633) · [專案頁](https://3dagentworld.github.io/opengs-slam/) | HKUST (GZ) | 點圖回歸加自適應尺度的戶外純 RGB Gaussian SLAM | ICRA 2025 | 34 | [215](https://github.com/3DAgentWorld/OpenGS-SLAM) |
| 主流 | 引用 | 2021 | [CoFiNet](https://arxiv.org/abs/2110.14076) | NUDT / TUM / Siemens | 由粗到細的對應：先在超點層級匹配再細化到點，不依賴重複性關鍵點 | NeurIPS 2021 | 385 | [138](https://github.com/haoyu94/Coarse-to-fine-correspondences) |
| 主流 | 引用 | 2024 | [CG-SLAM](https://arxiv.org/abs/2403.16095) · [專案頁](https://zju3dv.github.io/cg-slam) | Zhejiang | 不確定度感知且幾何一致的 Gaussian 場 RGB-D SLAM | ECCV 2024 | 104 | [125](https://github.com/hjr37/CG-SLAM) |
| 主流 | 引用 | 2023 | [EigenPlaces](https://arxiv.org/abs/2308.10832) | PoliTo | 依主成分方向分群取多視角訓練的視角穩健 VPR | ICCV 2023 | 183 | [163](https://github.com/gmberton/EigenPlaces) |
| 主流 | 引用 | 2025 | [S3PO-GS](https://arxiv.org/abs/2507.03737) · [專案頁](https://3dagentworld.github.io/S3PO-GS/) | HKUST (GZ) | 以 3DGS 點圖錨定追蹤避免尺度漂移的戶外單目 SLAM | ICCV 2025 | 38 | [137](https://github.com/3DAgentWorld/S3PO-GS) |
| 主流 | 引用 | 2022 | [ESLAM](https://arxiv.org/abs/2211.11704) · [專案頁](https://www.idiap.ch/paper/eslam/) | Idiap / EPFL / ams OSRAM | 多尺度軸對齊特徵平面表示 SDF 的高效稠密 SLAM | CVPR 2023 | 306 | [224](https://github.com/idiap/ESLAM) |
| 主流 | 引用 | 2023 | [R2Former](https://arxiv.org/abs/2304.03410) | ByteDance / UCF | 單一 Transformer 統一檢索與重排序的地點辨識 | CVPR 2023 | 175 | [104](https://github.com/bytedance/R2Former) |
| 主流 | 引用 | 2024 | [LIV-GaussMap](https://arxiv.org/abs/2401.14857) | HKUST / HKUST (GZ) 等 | LiDAR 慣性視覺融合的即時 Gaussian 輻射場建圖 | RA-L 2024 | 83 | [160](https://github.com/sheng00125/LIV-GaussMap) |
| 主流 | 引用、獲獎 | 2022 | [Active SLAM Survey](https://arxiv.org/abs/2207.00254) | Zaragoza / MIT SPARK / UCSD 等 | 主動 SLAM 與多機器人協作探索的綜述 | T-RO 2023 | 374 | 未公開 |
| 主流 | 引用 | 2023 | [LiDAR Odometry Survey](https://arxiv.org/abs/2312.17487) | SNU | 依感測器融合方式分類的 LiDAR 里程計綜述 | Intelligent Service Robotics 2024 | 156 | 未公開 |
| 新興 | 獲獎 | 2025 | [Back on Track](https://arxiv.org/abs/2504.14516) · [專案頁](https://wrchen530.github.io/projects/batrack/) | TUM / Oxford / Microsoft | 用 3D 點追蹤把動態點的運動拆成相機與物體分量，讓 BA 能直接處理動態影片 | ICCV 2025<br>oral | 26 | [105](https://github.com/wrchen530/batrack) |
| 新興 | 獲獎 | 2025 | [Ground-Optimized 4D Radar-Inertial Odometry](https://arxiv.org/abs/2502.08093) | SNU | 地面最佳化的雜訊濾除，加上以高斯過程連續積分速度的雷達慣性里程計 | ICRA 2025<br>入圍 Best Paper on Robot Perception | 13 | [109](https://github.com/wooseongY/Go-RIO) |
| 新興 | 獲獎 | 2022 | [Localizability Estimation](https://arxiv.org/abs/2203.05698) | ETH RSL | 從點雲直接學習各方向的可定位性，隧道等退化場景提前偵測並調整 LiDAR 定位 | IROS 2022<br>入圍 Best Paper | 54 | [101](https://github.com/leggedrobotics/L3E) |
| 新興 | 獲獎 | 2025 | [Doppler Correspondence](https://arxiv.org/abs/2502.11461) | UNIST / KAIST | 用 4D LiDAR／雷達的 Doppler 速度直接建立對應，掃描匹配不需迭代，在隧道、惡劣天氣更穩 | RSS 2025<br>入圍 Outstanding Student Paper | 6 | [46](https://github.com/Tars0523/Doppler_Correspondence) |
| 新興 | 獲獎 | 2025 | [FUSER](https://arxiv.org/abs/2512.09373) | NTU / Nanjing / Nankai / Alibaba | 一次處理所有掃描直接回歸全域位姿，免成對匹配，再以 SE(3)^N diffusion 精修 | CVPR 2026<br>入圍 Best Paper | 6 | 未公開 |

## 3D 場景重建（feed-forward、SfM、3DGS／NeRF）：超過主題上限

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 主流 | 引用、Star | 2024 | [3DGRT](https://arxiv.org/abs/2407.07090) · [專案頁](https://gaussiantracer.github.io/) | NVIDIA / Univ. of Toronto | 以 GPU 光線追蹤取代光柵化渲染 3D 高斯粒子 | SIGGRAPH Asia 2024 | 208 | [2,482](https://github.com/nv-tlabs/3dgrut) |
| 主流 | 引用、Star | 2024 | [3DGUT](https://arxiv.org/abs/2412.12507) · [專案頁](https://research.nvidia.com/labs/toronto-ai/3DGUT) | NVIDIA / Univ. of Toronto | 以無跡變換投影高斯，支援畸變相機與二次光線 | CVPR 2025 | 124 | [2,482](https://github.com/nv-tlabs/3dgrut) |
| 主流 | 引用、Star | 2025 | [SpatialTrackerV2](https://arxiv.org/abs/2507.12462) · [專案頁](https://spatialtracker.github.io) | Zhejiang / Oxford / Ant Group 等 | 統一點追蹤、深度與相機運動的前向 3D 追蹤 | ICCV 2025 | 104 | [1,007](https://github.com/henry123-boy/SpaTrackerV2) |
| 主流 | 引用、Star | 2025 | [WorldMirror](https://arxiv.org/abs/2510.10726) · [專案頁](https://3d-models.hunyuan.tencent.com/world/) | Tencent / CUHK / Zhejiang | 可注入任意幾何先驗並同時輸出多種 3D 表示 | ICML 2026 | 81 | [1,221](https://github.com/Tencent-Hunyuan/HunyuanWorld-Mirror) |
| 主流 | 引用、Star | 2024 | [SLAM3R](https://arxiv.org/abs/2412.09401) | PKU / HKU / Aalto 等 | 前饋點圖回歸逐窗重建的即時單目稠密重建 | CVPR 2025 | 141 | [1,381](https://github.com/PKU-VCL-3DV/SLAM3R) |
| 主流 | 引用、Star | 2024 | [DN-Splatter](https://arxiv.org/abs/2403.17822) · [專案頁](https://maturk.github.io/dn-splatter/) | ETH / Tampere / Aalto 等 | 以深度與法向量先驗約束 3DGS 並直接抽網格 | WACV 2025 | 224 | [849](https://github.com/maturk/dn-splatter) |
| 主流 | 引用、HF | 2025 | [STream3R](https://arxiv.org/abs/2508.10893) · [專案頁](https://nirvanalan.github.io/projects/stream3r/) | NTU / Shanghai AI Lab | 以因果 Transformer 串流預測 pointmap | ICLR 2026 | 96 | [413](https://github.com/NIRVANALAN/STream3R) |
| 主流 | 引用 | 2025 | [Point3R](https://arxiv.org/abs/2507.02863) · [專案頁](https://ykiwu.github.io/Point3R/) | Tsinghua | 以綁定 3D 位置的顯式指標記憶做串流重建 | NeurIPS 2025 | 98 | [202](https://github.com/YkiWu/Point3R) |
| 主流 | 引用 | 2025 | [Pow3R](https://arxiv.org/abs/2503.17316) · [專案頁](https://europe.naverlabs.com/pow3r) | Naver Labs / UCL | 可選擇輸入內參、位姿、深度先驗的前向重建 | CVPR 2025 | 82 | [245](https://github.com/naver/pow3r) |
| 主流 | 引用、Star | 2023 | [AdaPoinTr](https://arxiv.org/abs/2301.04545) | Tsinghua | PoinTr 加自適應查詢與去噪任務，補全更快更準，並延伸到場景級補全 | TPAMI 2023 | 199 | [870](https://github.com/yuxumin/PoinTr) |
| 主流 | 引用、獲獎 | 2025 | [RayZer](https://arxiv.org/abs/2505.00702) · [專案頁](https://hwjiang1510.github.io/RayZer/) | UT Austin / Adobe / Cornell 等 | 完全不用位姿或 3D 標註，自我預測相機後渲染新視角做自監督，訓練出大型視角合成模型 | ICCV 2025<br>🏆 Best Paper Honorable Mention | 90 | 未公開 |
| 主流 | 引用、Star | 2021 | [Shape As Points](https://arxiv.org/abs/2106.03452) · [專案頁](https://pengsongyou.github.io/sap) | MPI-IS / ETH / Tübingen 等 | 可微分 Poisson 求解器把點雲轉成隱式表面，比神經隱式表示快且可端到端最佳化 | NeurIPS 2021 | 316 | [643](https://github.com/autonomousvision/shape_as_points) |
| 主流 | 引用 | 2025 | [LONG3R](https://arxiv.org/abs/2507.18255) · [專案頁](https://zgchen33.github.io/LONG3R/) | Shanghai AI Lab / Tsinghua / Shanghai Qi Zhi | 記憶閘控與雙源注意力支撐長序列串流重建 | ICCV 2025 | 54 | [45](https://github.com/zgchen33/LONG3R) |
| 主流 | 引用 | 2025 | [Light3R-SfM](https://arxiv.org/abs/2501.14914) | NVIDIA / Vector Institute / Univ. of Toronto | 以可學習潛在全域對齊取代 BA 的前向 SfM | CVPR 2025 | 55 | 未公開 |
| 主流 | 引用 | 2025 | [Dynamic Point Maps](https://arxiv.org/abs/2503.16318) · [專案頁](https://www.robots.ox.ac.uk/~vgg/research/dynamic-point-maps/) | Oxford VGG | 把 DUSt3R 的點圖擴展為帶時間的動態點圖，一次得到動態場景的幾何與運動 | ICCV 2025 | 54 | 未公開 |
| 主流 | 引用 | 2021 | [SnowflakeNet](https://arxiv.org/abs/2108.04444) | Tsinghua / JD.com 等 | 以雪花式點反卷積逐步分裂點，skip-transformer 保留局部結構，補全細節更清楚 | ICCV 2021 | 375 | 未公開 |
| 主流 | 引用 | 2025 | [SuperPC](https://arxiv.org/abs/2503.14558) | University at Buffalo | 單一 diffusion 模型同時處理點雲補全、上採樣、去噪與上色，避免各任務串接誤差 | CVPR 2025 | 32 | [25](https://github.com/sair-lab/SuperPC) |
| 新興 | 獲獎 | 2025 | [FastMap](https://arxiv.org/abs/2505.04612) · [專案頁](https://jiahao.ai/fastmap) | TTIC / Toyota Research Institute | 只用一階最佳化的全域 SfM，GPU 上比 COLMAP、GLOMAP 快約 10 倍、位姿精度相當 | 3DV 2026<br>入圍 Best Paper | 7 | [292](https://github.com/pals-ttic/fastmap) |
| 新興 | 獲獎 | 2021 | [Learning to Solve Hard Minimal Problems](https://arxiv.org/abs/2112.03424) | Georgia Tech / CTU Prague | 學習挑選起始問題解對做同倫延拓，只算出需要的那個解，大幅加速難的最小問題求解 | CVPR 2022<br>🏆 Best Paper | 45 | [146](https://github.com/petrhruby97/learning_minimal) |
| 新興 | 獲獎 | 2025 | [Anisotropic Rotation Averaging](https://arxiv.org/abs/2503.07353) | Lund / Chalmers | 把量測的各向異性不確定性放進旋轉平均，並給出可驗證全域最優的鬆弛解 | ICCV 2025<br>oral | 3 | [11](https://github.com/ylochman/anisotropic-ra) |

## 深度估計與 occupancy：新興滿兩年未達門檻

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 新興 | 獲獎 | 2021 | [Neural Disparity Refinement](https://arxiv.org/abs/2110.15367) · [專案頁](https://cvlab-unibo.github.io/neural-disparity-refinement-web) | Bologna | 連續式視差精修網路，可輸出任意解析度，適合手機上高低解析度不對稱的雙目 | 3DV 2021<br>oral | 36 | [63](https://github.com/CVLAB-Unibo/neural-disparity-refinement) |
| 新興 | 獲獎 | 2021 | [Binary TTC](https://arxiv.org/abs/2101.04777) | NVIDIA / UCSB | 把碰撞時間估計改成逐像素二元分類（是否在時限內碰撞），單目、免校正即可當時間柵欄 | CVPR 2021<br>入圍 Best Student Paper Honorable Mention | 40 | 未公開 |

## 深度估計與 occupancy：超過主題上限

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 主流 | 引用、Star | 2025 | [Prior Depth Anything](https://arxiv.org/abs/2505.10565) · [專案頁](https://prior-depth-anything.github.io/) | Zhejiang / HKU | 融合任意稀疏公制先驗與相對深度預測補全深度 | arXiv | 50 | [536](https://github.com/SpatialVision/Prior-Depth-Anything) |
| 主流 | 引用 | 2025 | [Depth Any Camera](https://arxiv.org/abs/2501.02464) · [專案頁](https://yuliangguo.github.io/depth-any-camera) | Bosch / CMU / Simon Fraser 等 | 透視相機訓練即可泛化到魚眼與 360 度公制深度 | CVPR 2025 | 58 | [363](https://github.com/yuliangguo/depth_any_camera) |
| 主流 | 引用 | 2024 | [IGEV++](https://arxiv.org/abs/2409.00638) | HUST | 多範圍幾何編碼體積處理大視差與病態區域 | TPAMI 2025 | 131 | [330](https://github.com/gangweix/igev-plusplus) |
| 主流 | 引用 | 2025 | [EmbodiedOcc++](https://arxiv.org/abs/2504.09540) · [專案頁](https://pkuhaowang.github.io/EmbodiedOcc2/) | PKU | 平面正則與不確定性取樣改進室內高斯佔據預測 | ACM MM 2025 | 38 | [35](https://github.com/PKUHaoWang/EmbodiedOcc2) |
| 主流 | 引用 | 2025 | [MonSter++](https://arxiv.org/abs/2501.08643) | HUST | 單眼深度先驗雙分支融合，統一雙目與多視角立體 | TPAMI 2026 | 38 | 未公開 |
| 新興 | 獲獎 | 2025 | [Zero-Shot Scene Flow](https://arxiv.org/abs/2501.10357) · [專案頁](https://research.nvidia.com/labs/lpr/zero_msf/) | NVIDIA / Brown | 聯合估幾何與運動並大規模混合資料訓練，單目場景流首次能 zero-shot 泛化 | CVPR 2025<br>入圍 Best Paper | 24 | 未公開 |
| 新興 | 獲獎 | 2025 | [DiFuse-Net](https://arxiv.org/abs/2506.14709) | Samsung Research India | 把 RGB 與手機雙像素（dual-pixel）分開編碼後以雙向視差注意力融合估深度 | IROS 2025<br>入圍 Award Finalist | 0 | 未公開 |

## 3D 偵測與分割（點雲骨幹、3D 偵測、語意／實例分割）：新興滿兩年未達門檻

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 新興 | 獲獎 | 2022 | [InterObject3D](https://arxiv.org/abs/2204.07183) | ETH / RWTH Aachen | 使用者點擊迭代修正的互動式 3D 實例分割，可泛化到訓練外類別 | ICRA 2023<br>入圍 Outstanding Physical HRI Paper | 36 | [42](https://github.com/theodorakontogianni/InterObject3D) |
| 新興 | 獲獎 | 2021 | [Category-level Pose and Shape](https://arxiv.org/abs/2104.08383) | MIT | 給類別 CAD 庫的主動形狀模型，以可驗證全域最優的凸鬆弛同時解物件位姿與形狀，對離群點穩健 | RSS 2021<br>入圍 Best Paper | 29 | 未公開 |
| 新興 | 獲獎 | 2024 | [HEGN](https://doi.org/10.1109/ICRA57147.2024.10610562) | Siemens / TUM | 階層式等變圖網路做含縮放的 9DoF 點雲配準，用於類別級位姿估計 | ICRA 2024<br>入圍 Best Conference Paper | 1 | 未公開 |

## 3D 偵測與分割（點雲骨幹、3D 偵測、語意／實例分割）：超過主題上限

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 主流 | 引用 | 2024 | [MaskClustering](https://arxiv.org/abs/2401.07745) · [專案頁](https://pku-epic.github.io/MaskClustering/) | PKU / BAAI / Galbot | 以視角共識率做遮罩圖分群的開放詞彙 3D 實例分割 | CVPR 2024 | 85 | [134](https://github.com/PKU-EPIC/MaskClustering) |
| 新興 | 獲獎 | 2025 | [Chorus](https://arxiv.org/abs/2512.17817) · [專案頁](https://gaussianworld.github.io/Chorus) | Amsterdam / ETH / INSAIT | 從多個 2D 基礎模型蒸餾，學出 feed-forward 的 3DGS 場景編碼器，提供通用 3D 特徵 | CVPR 2026<br>入圍 Best Paper | 13 | 未公開 |
| 新興 | 獲獎 | 2025 | [SNAP](https://arxiv.org/abs/2510.11565) · [專案頁](https://neu-vi.github.io/SNAP/) | Northeastern / MathWorks | 跨室內、室外、空拍點雲的互動式 3D 分割，同時支援點選與文字提示 | 3DV 2026<br>入圍 Best Paper | 0 | 未公開 |

## 3D 空間理解（3D grounding、空間推理 VLM、3D-LLM）：超過主題上限

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 主流 | 引用 | 2023 | [LL3DA](https://arxiv.org/abs/2311.18651) · [專案頁](https://ll3da.github.io/) | Fudan / Tencent PCG / NUS | 直接吃點雲並接受點擊、框選等視覺提示的 3D 助理，做描述、問答與規劃 | CVPR 2024 | 301 | [321](https://github.com/Open3DA/LL3DA) |
| 主流 | 引用 | 2025 | [Inst3D-LMM](https://arxiv.org/abs/2503.00513) | Zhejiang | 以實例為單位融合 2D 語意與 3D 幾何，一個模型做多種 3D 理解任務 | CVPR 2025 | 65 | [134](https://github.com/hanxunyu/Inst3D-LMM) |
| 主流 | 引用 | 2025 | [G2VLM](https://arxiv.org/abs/2511.21688) · [專案頁](https://gordonhu608.github.io/g2vlm.github.io/) | Shanghai AI Lab / HKU 等 | 同一個 VLM 同時做 3D 重建與空間推理，幾何特徵直接支援問答 | arXiv | 49 | [362](https://github.com/InternRobotics/G2VLM) |
| 主流 | 引用、HF | 2025 | [MindJourney](https://arxiv.org/abs/2507.12508) · [專案頁](https://umass-embodied-agi.github.io/MindJourney/) | UMass Amherst / JHU / Microsoft 等 | 推理時用影片 world model 想像換視角後的畫面，提升 VLM 空間推理，不需重新訓練 | NeurIPS 2025 | 60 | [155](https://github.com/UMass-Embodied-AGI/MindJourney) |
| 主流 | 引用 | 2025 | [Locate 3D](https://arxiv.org/abs/2504.14151) · [專案頁](https://locate3d.atmeta.com/) | Meta FAIR | 以 3D-JEPA 自監督學習點雲特徵，依指代語句在真實 RGB-D 感測資料中定位物件，可上機器人 | ICML 2025 | 32 | [456](https://github.com/facebookresearch/locate-3d) |
| 主流 | 引用 | 2024 | [SeeGround](https://arxiv.org/abs/2412.04383) · [專案頁](https://seeground.github.io/) | HKUST(GZ) / NUS / A*STAR | 零樣本 3D grounding：選視角渲染畫面加物件位置文字，交給 2D VLM 判斷 | CVPR 2025 | 96 | [224](https://github.com/iris0329/SeeGround) |
| 主流 | 引用 | 2024 | [PQ3D](https://arxiv.org/abs/2405.11442) · [專案頁](https://pq3d.github.io) | Tsinghua / BIGAI | 可提示查詢的統一 3D 視覺語言模型，同時吃點雲、多視角影像等多種場景表示 | ECCV 2024 | 107 | 未公開 |
| 主流 | 引用 | 2025 | [SR-3D](https://arxiv.org/abs/2509.13317) · [專案頁](https://www.anjiecheng.me/sr3d) | UC San Diego / MIT / NVIDIA | 在 2D 特徵加 3D 位置編碼，可在任一視角框選區域並跨視角推理 | ICLR 2026 | 33 | [32](https://github.com/AnjieCheng/SR-3D) |
| 主流 | 引用 | 2025 | [3DLLM-Mem](https://arxiv.org/abs/2505.22657) · [專案頁](https://3dllm-mem.github.io) | UCLA / Google Research | 給具身 3D LLM 長期時空記憶，在多房間任務中選擇性取用過去觀察 | NeurIPS 2025 | 33 | 未公開 |

## 電腦視覺（偵測、分割、視覺基礎模型）：新興滿兩年未達門檻

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 新興 | 獲獎 | 2024 | [Evidential OOD Segmentation](https://doi.org/10.1109/ICRA57147.2024.10611342) | MIT / ARL | 不需 OOD 樣本，以證據式深度學習估計語意分割的逐像素不確定性，偵測未知障礙 | ICRA 2024<br>入圍 Best Paper in Robot Vision | 26 | 未公開 |

## 電腦視覺（偵測、分割、視覺基礎模型）：超過主題上限

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 主流 | 引用、Star | 2023 | [SAM-Track](https://arxiv.org/abs/2305.06558) | Zhejiang | SAM 結合 DeAOT 的多模態互動影片分割追蹤 | arXiv | 285 | [3,146](https://github.com/z-x-yang/Segment-and-Track-Anything) |
| 主流 | 引用、Star | 2025 | [DEIMv2](https://arxiv.org/abs/2509.20787) · [專案頁](https://intellindust-ai-lab.github.io/projects/DEIMv2/) | Intellindust / Xiamen | DEIM 接上 DINOv3 特徵，涵蓋 GPU 到行動端 | arXiv | 75 | [2,083](https://github.com/Intellindust-AI-Lab/DEIMv2) |
| 主流 | 引用、Star | 2023 | [AM-RADIO](https://arxiv.org/abs/2312.06709) | NVIDIA | 多教師蒸餾融合 CLIP、DINOv2、SAM 的單一骨幹 | CVPR 2024 | 224 | [1,989](https://github.com/NVlabs/RADIO) |
| 主流 | 引用、Star | 2024 | [RADIOv2.5](https://arxiv.org/abs/2412.07679) | NVIDIA | 解決解析度模式切換並擴大規模的聚合骨幹 | CVPR 2025 | 117 | [1,989](https://github.com/NVlabs/RADIO) |
| 主流 | 引用、Star | 2024 | [DINO-X](https://arxiv.org/abs/2411.14347) | IDEA | 支援免提示的開放世界偵測與理解統一模型 | arXiv | 124 | [1,427](https://github.com/IDEA-Research/DINO-X-API) |
| 主流 | 引用、Star | 2025 | [RoMa v2](https://arxiv.org/abs/2511.15706) | Linköping / Chalmers / Amsterdam 等 | 改良架構與訓練，更快更準的稠密匹配 | ECCV 2026 | 67 | [759](https://github.com/Parskatt/romav2) |
| 主流 | 引用 | 2025 | [AllTracker](https://arxiv.org/abs/2506.07310) · [專案頁](https://alltracker.github.io) | Stanford / CMU / TRI 等 | 以多幀光流估計做高解析度全像素點追蹤 | ICCV 2025 | 74 | [437](https://github.com/aharley/alltracker) |
| 主流 | 引用、Star | 2025 | [EdgeTAM](https://arxiv.org/abs/2501.07256) | Meta / NTU | 2D 空間感知器壓縮記憶，讓 SAM 2 手機即時 | CVPR 2025 | 34 | [1,013](https://github.com/facebookresearch/EdgeTAM) |
| 主流 | 引用、Star | 2024 | [OmniGlue](https://arxiv.org/abs/2405.12979) · [專案頁](https://hwjiang1510.github.io/OmniGlue) | UT Austin / Google | 用 DINOv2 引導關鍵點匹配，提升跨域泛化 | CVPR 2024 | 126 | [711](https://github.com/google-research/omniglue) |
| 主流 | 引用、Star | 2025 | [RT-DETRv4](https://arxiv.org/abs/2510.25257) | PKU | 訓練時蒸餾基礎模型特徵，推論零額外成本 | ECCV 2026 | 40 | [674](https://github.com/RT-DETRs/RT-DETRv4) |
| 主流 | 引用、Star | 2024 | [LW-DETR](https://arxiv.org/abs/2406.03459) | Baidu / Adelaide / Beihang 等 | ViT 編碼器加淺層解碼器，取代 YOLO 的即時 DETR | arXiv | 102 | [514](https://github.com/Atten4Vis/LW-DETR) |
| 主流 | 引用 | 2022 | [DKM](https://arxiv.org/abs/2202.00667) · [專案頁](https://parskatt.github.io/DKM/) | Linköping | 核回歸全域匹配加深度引導細化的稠密匹配 | CVPR 2023 | 310 | [490](https://github.com/Parskatt/DKM) |
| 主流 | 引用、HF | 2024 | [Theia](https://arxiv.org/abs/2407.20179) · [專案頁](http://theia.theaiinstitute.com) | Stony Brook / The AI Institute | 蒸餾多個視覺基礎模型成機器人學習用小模型 | CoRL 2024 | 91 | [288](https://github.com/bdaiinstitute/theia) |
| 新興 | 獲獎 | 2023 | [OvSGTR](https://arxiv.org/abs/2311.10988) | CASIA / PolyU | 物件與關係都開放詞彙的場景圖生成，以視覺概念對齊並保留知識避免遺忘 | ECCV 2024<br>入圍 Best Paper | 50 | [104](https://github.com/gpt4vision/OvSGTR) |
| 新興 | 獲獎 | 2025 | [LAPA](https://arxiv.org/abs/2512.04213) · [專案頁](https://ostadabbas.github.io/lapa.github.io/) | Northeastern | 端到端 transformer 同時做外觀匹配與幾何約束，多相機點追蹤不再拆成偵測、關聯、追蹤 | 3DV 2026<br>🏆 Best Paper | 5 | [8](https://github.com/ostadabbas/Look-Around-and-Pay-Attention-LAPA-) |

## 模擬與 Real2Sim：新興滿兩年未達門檻

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 新興 | 獲獎 | 2022 | [NeRF2Real](https://arxiv.org/abs/2210.04932) · [專案頁](https://sites.google.com/view/nerf2real/home) | DeepMind | 手機影片建 NeRF 取得接觸幾何與新視角渲染，在模擬中訓練視覺策略後轉移到實機 | ICRA 2023<br>入圍 Outstanding Robot Learning Paper | 80 | 未公開 |

## 模擬與 Real2Sim：超過主題上限

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 主流 | 引用、機構 | 2025 | [Re3Sim](https://arxiv.org/abs/2502.08645) · [專案頁](http://xshenhan.github.io/Re3Sim/) | SJTU / Shanghai AI Lab / HKU | 3D 重建加神經渲染的照片級 real2sim 資料生成 | ICRA 2026 | 68 | [185](https://github.com/OpenRobotLab/Re3Sim) |
| 主流 | 引用、機構 | 2024 | [ACDC](https://arxiv.org/abs/2410.07408) · [專案頁](https://digital-cousins.github.io) | Stanford | 用相似而非精確複製的數位表親場景訓練穩健策略 | CoRL 2024 | 154 | [255](https://github.com/cremebrule/digital-cousins) |
| 主流 | 引用 | 2025 | [Vid2Sim](https://arxiv.org/abs/2501.06693) · [專案頁](https://metadriverse.github.io/vid2sim/) | UCLA / UIUC | 從影片重建可互動 3DGS 城市環境訓練導航 | CVPR 2025 | 53 | [295](https://github.com/Vid2Sim/Vid2Sim) |
| 主流 | 引用 | 2024 | [Articulate-Anything](https://arxiv.org/abs/2410.13882) · [專案頁](https://articulate-anything.github.io/) | UPenn | VLM 生成程式碼並自我批評建立關節物件 | ICLR 2025 | 133 | [229](https://github.com/vlongle/articulate-anything) |
| 主流 | 引用、HF | 2025 | [Veo World Simulator](https://arxiv.org/abs/2512.10675) · [專案頁](https://veo-robotics.github.io/) | Google DeepMind | 把 Veo 影片模型改成以動作為條件、多視角一致的世界模擬器，用來排序策略、測 OOD 泛化與紅隊找不安全行為；1600+ 次實機評估顯示預測與實際成功率高度相關 | arXiv | 63 | 未公開 |
| 主流 | 引用、機構 | 2025 | [Scalable Real2Sim](https://arxiv.org/abs/2503.00370) · [專案頁](https://scalable-real2sim.github.io/) | MIT | 機器人抓放自動辨識幾何與慣性參數產生模擬資產 | IROS 2025 | 52 | [167](https://github.com/nepfaff/scalable-real2sim) |
| 主流 | 引用 | 2025 | [Reality Gap Review](https://arxiv.org/abs/2510.20808) | UZH / NVIDIA / UW | 整理 sim-to-real 落差來源與對策的綜述 | ARCRAS 2026 | 57 | 未公開 |
| 主流 | 引用 | 2025 | [DRAWER](https://arxiv.org/abs/2504.15278) · [專案頁](https://drawer-art.github.io/) | UIUC / UW / AI2 等 | 單段影片轉成可互動關節的照片級室內環境 | CVPR 2025 | 41 | [176](https://github.com/xiahongchi/DRAWER) |
| 主流 | 引用 | 2024 | [SplatSim](https://arxiv.org/abs/2409.10161) · [專案頁](https://splatsim.github.io) | CMU | 用 3DGS 取代模擬器渲染，縮小視覺 sim-to-real 差距 | ICRA 2025 | 109 | [162](https://github.com/qureshinomaan/SplatSim) |
| 主流 | 引用 | 2025 | [ArticulatedGS](https://arxiv.org/abs/2503.08135) | USTC / NUDT | 兩種關節狀態影像自監督重建關節物件 3DGS | CVPR 2025 | 48 | 未公開 |
| 主流 | 引用、機構 | 2025 | [GSWorld](https://arxiv.org/abs/2510.20813) · [專案頁](https://3dgsworld.github.io) | UCSD / UCLA / Meta | GSDF 格式結合 3DGS 與物理引擎的閉環操作模擬 | ICRA 2026 | 34 | [232](https://github.com/luccachiang/GSWorld) |
| 主流 | 引用 | 2025 | [MetaScenes](https://arxiv.org/abs/2505.02388) · [專案頁](https://meta-scenes.github.io/) | BIGAI | 自動把真實掃描物件替換成可模擬資產 | CVPR 2025 | 40 | [69](https://github.com/meta-scenes/MetaScenes) |
| 主流 | 引用 | 2024 | [DigitalTwinArt](https://arxiv.org/abs/2404.01440) · [專案頁](https://nvlabs.github.io/DigitalTwinArt/) | NVIDIA / Stanford | 兩次 RGBD 掃描重建未知關節物件數位分身 | CVPR 2024 | 94 | [74](https://github.com/NVlabs/DigitalTwinArt) |
