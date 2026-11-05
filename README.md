# Robot Perception Survey

AMR、四足、輪足機器人的導航、視覺、3D 感知、SLAM、Real2Sim，以及 AMR 加手臂（移動操作）的感知前沿論文整理，每週一、四自動更新。

<!-- 本檔由 scripts/build_readme.py 產生，請改 topics/、data/ 或 digests/ 後重跑 -->

- 每週一、四由排程 agent 依 [update-survey](.claude/skills/update-survey/SKILL.md) 的流程搜尋新論文並開 PR，`build_readme.py` 通過後自動 merge。
- 手動更新：在 repo 裡開 Claude Code，說「更新論文整理」。
- 每個主題分三段：在解決的問題、重要論文（2021 年起，開創性的不限年份）、最新論文（最近 3 個月，更早的留在主題檔）。
- 程式碼標「未公開」：論文頁、arXiv 頁與 GitHub 搜尋都找不到作者釋出的官方程式碼（第三方重現不算）。

## 怎樣算重要論文

符合任一條就收錄，「理由」欄標出符合哪幾條：

| 理由 | 條件 |
|---|---|
| 引用 | 引用數達年份門檻：2021–22 年 ≥ 300、2023 年 ≥ 150、2024 年 ≥ 80、2025 年 ≥ 30（Semantic Scholar） |
| Star | 官方 repo star ≥ 500 |
| HF | Hugging Face Papers 按讚數 ≥ 20 |
| 獲獎 | 頂會最佳論文（含入圍）或 oral，或刊在 Science Robotics、T-RO |
| 基準 | 提出被廣泛採用的 benchmark、資料集，或常被當比較基準的方法 |
| 機構 | [定期追蹤的來源](#定期追蹤的來源)的企業與[實驗室主要名單](docs/labs.md#主要名單)內機構發表，且有實機實驗與開源 |
| 推薦 | 人工推薦 |
| 知名 | 人工認定的代表性方法，不封存也不佔主題上限 |

候選由 `scripts/harvest.py` 依主題關鍵字從 Semantic Scholar 撈出，再人工確認相關性；頂會得獎名單另外逐一查官網補收。只有 arXiv 預印本的，只收[定期追蹤的來源](#定期追蹤的來源)的企業與[實驗室主要名單](docs/labs.md#主要名單)內機構的論文，且首次公開超過一年仍未刊登就移出；官方 repo star ≥ 500 或人工推薦的除外。分級：**奠基** 引用達門檻 4 倍、star ≥ 10k，或 2021 年前的開創性論文；**主流** 達引用或 Star 條件；其餘（只符合獲獎、基準、機構、推薦、知名）為**新興**。同一級內依分數（「引用 ÷ 該年門檻」加「star ÷ 500」）由高到低排序。「年」是 arXiv 首次公開年份，「來源」是正式刊登的會議或期刊。

為了控制篇數，符合下列條件的論文移到[封存區](docs/archive.md)，不刪除；標「推薦」「基準」「知名」的不封存。

- 新興論文公開滿兩個年度，引用與 star 都仍未滿 100。
- 主題超過 30 篇時，封存分數最低的，奠基論文與當年度論文不納入淘汰。

## 定期追蹤的來源

完整查法與關鍵字見 [sources.md](.claude/skills/update-survey/sources.md)。

- **NVIDIA Research**（每次必查）：[Robotics](https://research.nvidia.com/research-area/robotics)、[Computer Vision](https://research.nvidia.com/research-area/computer-vision)、[Seattle Robotics Lab](https://research.nvidia.com/labs/srl)、[GEAR](https://research.nvidia.com/labs/gear/)、[NVlabs GitHub](https://github.com/NVlabs)
- **企業**：Google DeepMind、Meta FAIR、Physical Intelligence、Skild AI、Mistral、Alibaba、ByteDance Seed、Tencent Robotics X、Huawei、Unitree、LimX、ANYbotics、Boston Dynamics、Waymo、Sony AI、Adobe、Samsung、Baidu、Microsoft、Apple
- **實驗室**：[追蹤的實驗室](docs/labs.md)，分主要名單與擴充追蹤（只用來找論文，不影響收錄條件）
- **arXiv**：cs.RO、cs.CV 的每日 RSS 與 API，依主題關鍵字查上次更新後的新投稿
- **Hugging Face Daily Papers**：社群每日精選，按讚數是收錄條件之一
- **期刊**：Science Robotics、T-RO、IJRR、RA-L、T-ASE、JFR、TPAMI、IJCV
- **會議**（接收論文公布時）：RSS、CoRL、ICRA、IROS、CVPR、ICCV、ECCV、3DV、SIGGRAPH、WACV、NeurIPS、ICLR、ICML；EMNLP、ACL（只看 VLN）

最後更新：2026-11-05

## 目錄

- [本月趨勢（2026-11）](#本月趨勢2026-11)
- [VLN 與導航基礎模型](#vln-與導航基礎模型)
- [局部導航與規劃（diffusion / world model / 探索）](#局部導航與規劃diffusion--world-model--探索)
- [移動操作感知（導航銜接、抓取、物件遞交）](#移動操作感知導航銜接抓取物件遞交)
- [SLAM 與定位](#slam-與定位)
- [3D 場景重建（feed-forward、SfM、3DGS／NeRF）](#3d-場景重建feed-forwardsfm3dgsnerf)
- [深度估計與 occupancy](#深度估計與-occupancy)
- [語意地圖與場景圖](#語意地圖與場景圖)
- [3D 偵測與分割（點雲骨幹、3D 偵測、語意／實例分割）](#3d-偵測與分割點雲骨幹3d-偵測語意實例分割)
- [3D 空間理解（3D grounding、空間推理 VLM、3D-LLM）](#3d-空間理解3d-grounding空間推理-vlm3d-llm)
- [電腦視覺（偵測、分割、視覺基礎模型）](#電腦視覺偵測分割視覺基礎模型)
- [模擬與 Real2Sim](#模擬與-real2sim)
- [月報](#月報)
- [四足與輪足](docs/legged.md)
- [追蹤的實驗室](docs/labs.md)
- [封存區](docs/archive.md)

## 本月趨勢（2026-11）

- 觀察：導航 world model 在 ECCV 2026 成為明顯方向（RAE-NWM、UniWM），開始比較不同表示空間，不再只用 VAE latent。
- 觀察：feed-forward 模型往「固定記憶體的串流」與「SLAM 前端」發展（OVGGT、FILT3R、UniSim-SLAM），也開始用在 VIO 初始化（FF-VIO-Init）。
- 觀察：這批補收的 VLN 多半把語言模型當高層決策，再接上幾何或技能層（OpenFrontier、AgentVLN）。
- 推測：固定記憶體的串流重建可望讓長時間建圖上機；可在 Jetson 上跑長序列、量記憶體與延遲驗證。
- 觀察：移動操作的瓶頸集中在最後一段抓取：FOUND-IT++ 上機導航到物件 100%，抓取只有 50%，作者歸因於缺主動深度回饋；HoMMI 的消融實驗中，只用腕部或只用頭部相機都大幅掉分（Delivery 15%、5%，完整 85%）。
- 推測：導航可以用輕量單目地圖，但抓取仍需要腕部或主動深度；可在同一台車上固定抓取模型，比較有無腕部深度的抓取成功率驗證。

## VLN 與導航基礎模型

### 在解決的問題

- 語言對應到空間：把「走到廚房冰箱旁」對到畫面與地圖上的位置。
- 長程、部分可觀測：指令長、環境沒看過，需要記憶與探索。
- sim-to-real：benchmark 多在 Habitat 模擬，實機成功率落差大。
- 推論延遲：數 B 參數的 VLM 難以機上即時跑，近期多改成「慢 VLM 推理 + 快控制層」。
- 跨機體：同一模型用在輪式、四足、人形。

### 重要論文（資料日期 2026-11-01）

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 奠基 | Star、基準、推薦 | 2017 | [R2R](https://arxiv.org/abs/1711.07280) · [專案頁](https://bringmeaspoon.org/) | ANU / Adelaide / QUT 等 | R2R 資料集與 Matterport3D 模擬器，開創 VLN | CVPR 2018 | 2,087 | [718](https://github.com/peteanderson80/Matterport3DSimulator) |
| 奠基 | 引用、Star、HF、機構 | 2025 | [StreamVLN](https://arxiv.org/abs/2507.05240) · [專案頁](https://streamvln.github.io/) | Shanghai AI Lab / Zhejiang / SJTU 等 | SlowFast 上下文加 KV cache 重用做串流 VLN | ICRA 2026 | 193 | [639](https://github.com/OpenRobotLab/StreamVLN) |
| 奠基 | 引用、Star、推薦 | 2024 | [NaVILA](https://arxiv.org/abs/2412.04453) · [專案頁](https://navila-bot.github.io/) | UCSD / NVIDIA | VLM 輸出中層語言動作，低層腿式運動策略執行 | RSS 2025 | 354 | [729](https://github.com/AnjieCheng/NaVILA) |
| 奠基 | 引用、Star | 2025 | [JanusVLN](https://arxiv.org/abs/2509.22548) · [專案頁](https://miv-xjtu.github.io/JanusVLN.github.io/) | Xi'an Jiaotong / Alibaba | 語意與空間幾何拆成雙隱式記憶，固定大小免記憶膨脹 | ICLR 2026 | 139 | [603](https://github.com/MIV-XJTU/JanusVLN) |
| 奠基 | 引用 | 2024 | [NaVid](https://arxiv.org/abs/2402.15852) · [專案頁](https://pku-epic.github.io/NaVid/) | PKU | 只用單眼 RGB 影片的 VLM 做 VLN，不需地圖與深度 | RSS 2024 | 355 | [458](https://github.com/jzhzhang/NaVid-VLN-CE) |
| 奠基 | 引用 | 2025 | [UniGoal](https://arxiv.org/abs/2503.10630) · [專案頁](https://bagh2178.github.io/UniGoal/) | Tsinghua / NTU | 統一圖表示把類別、影像、文字目標做零樣本導航 | CVPR 2025 | 128 | [371](https://github.com/bagh2178/UniGoal) |
| 奠基 | Star、基準、推薦 | 2020 | [VLN-CE](https://arxiv.org/abs/2004.02857) · [專案頁](https://jacobkrantz.github.io/vlnce) | Oregon State / Georgia Tech / Meta | VLN 從導航圖移到連續環境底層動作 | ECCV 2020 | 736 | [899](https://github.com/jacobkrantz/VLN-CE) |
| 奠基 | 獲獎 | 2020 | [3D-MOS (Multi-Resolution POMDP)](https://arxiv.org/abs/2005.02878) | Brown / MIT | 多解析度八叉樹信念的 POMDP，在 3D 空間有效率地搜尋多個目標物件 | IROS 2021 | 32 | 未公開 |
| 主流 | 引用、Star、HF、機構、推薦 | 2025 | [DualVLN](https://arxiv.org/abs/2512.08186) · [專案頁](https://internrobotics.github.io/internvla-n1-dualvln.github.io/) | Shanghai AI Lab / Zhejiang / Tsinghua 等 | VLM 慢速預測路徑點、輕量策略快速執行的雙系統 VLN | arXiv | 109 | [1,161](https://github.com/InternRobotics/InternNav) |
| 主流 | 引用、Star、獲獎、推薦 | 2023 | [VLFM](https://arxiv.org/abs/2312.03275) · [專案頁](http://naoki.io/vlfm) | Boston Dynamics AI Institute | VLM 算語意價值地圖引導 frontier 探索，Spot 實機 zero-shot 物件導航 | ICRA 2024 | 469 | [832](https://github.com/bdaiinstitute/vlfm) |
| 主流 | 引用、知名 | 2023 | [NavGPT](https://arxiv.org/abs/2305.16986) | Adelaide / ANU | 純 LLM 推理做 VLN，把觀測轉文字 | AAAI 2024 | 514 | [356](https://github.com/GengzeZhou/NavGPT) |
| 主流 | 引用、知名 | 2024 | [SG-Nav](https://arxiv.org/abs/2410.08189) · [專案頁](https://bagh2178.github.io/SG-Nav/) | Tsinghua / BUPT | 線上 3D 場景圖分層提示 LLM 做零樣本物件導航 | NeurIPS 2024 | 243 | [357](https://github.com/bagh2178/SG-Nav) |
| 主流 | 引用、推薦 | 2025 | [MapNav](https://arxiv.org/abs/2502.13451) | HKUST(GZ) / BAAI / Tsinghua | 標註語意俯視地圖取代歷史影格當 VLM 記憶 | ACL 2025 | 99 | [34](https://github.com/linglingxiansen/MapNav) |
| 主流 | 引用、知名 | 2022 | [LM-Nav](https://arxiv.org/abs/2207.04429) · [專案頁](https://sites.google.com/view/lmnav) | UC Berkeley | 用現成 LLM + VLM + ViNT 類導航模型組合，不需標註語言資料就能照指令走 | CoRL 2022 | 833 | [272](https://github.com/blazejosinski/lm_nav) |
| 主流 | 引用、知名 | 2023 | [ETPNav](https://arxiv.org/abs/2304.03047) | UCAS / CASIA 等 | 連續環境 VLN 用線上拓撲圖做高層規劃 | TPAMI 2024 | 315 | [499](https://github.com/MarSaKi/ETPNav) |
| 主流 | 引用、推薦 | 2025 | [NavMorph](https://arxiv.org/abs/2506.23468) | CASIA / UCAS | 隱空間自我演化世界模型，導航中線上適應環境 | ICCV 2025 | 67 | [96](https://github.com/Feliciaxyao/NavMorph) |
| 主流 | 引用、基準 | 2024 | [GOAT-Bench](https://arxiv.org/abs/2404.06609) · [專案頁](https://mukulkhanna.github.io/goat-bench) | Georgia Tech / CMU / UIUC 等 | 多模態目標的終身導航基準 | CVPR 2024 | 162 | [166](https://github.com/Ram81/goat-bench) |
| 主流 | 引用、推薦 | 2024 | [VLN Foundation Model Survey](https://arxiv.org/abs/2407.07035) | Michigan State / UMich / UNC 等 | 以規劃推理框架整理基礎模型時代的 VLN 方法 | TMLR 2024 | 123 | [307](https://github.com/zhangyuejoslin/VLN-Survey-with-Foundation-Models) |
| 主流 | Star、推薦 | 2022 | [VLN Survey](https://arxiv.org/abs/2203.12667) | UC Santa Cruz / Adelaide / USC | 依溝通複雜度與任務目標分類整理 VLN 任務與方法 | ACL 2022 | 216 | [611](https://github.com/UCSB-AI/awesome-vision-language-navigation) |
| 主流 | 引用、基準 | 2024 | [HM3D-OVON](https://arxiv.org/abs/2409.14296) · [專案頁](http://naoki.io/portfolio/ovon.html) | Georgia Tech / Meta | 379 類開放詞彙物件導航資料集與基準 | IROS 2024 | 131 | [152](https://github.com/naokiyokoyama/ovon) |
| 主流 | 引用、知名 | 2021 | [HAMT](https://arxiv.org/abs/2110.13309) · [專案頁](https://cshizhe.github.io/projects/vln_hamt.html) | Inria / ENS | 階層式 ViT 編碼完整全景歷史取代 RNN 記憶 | NeurIPS 2021 | 446 | [153](https://github.com/cshizhe/VLN-HAMT) |
| 主流 | 引用、獲獎、基準 | 2023 | [ScaleVLN](https://arxiv.org/abs/2307.15644) | Shanghai AI Lab / Adelaide / UNC 等 | 用 1200+ 場景合成 490 萬筆 VLN 訓練資料 | ICCV 2023 | 196 | [228](https://github.com/wz0919/ScaleVLN) |
| 主流 | 引用、獲獎、知名 | 2022 | [DUET](https://arxiv.org/abs/2202.11742) · [專案頁](https://cshizhe.github.io/projects/vln_duet.html) | Inria / ENS / IIIT Hyderabad | 線上拓撲圖做全域規劃，搭配局部細粒度跨模態推理 | CVPR 2022 | 333 | [294](https://github.com/cshizhe/VLN-DUET) |
| 主流 | 引用、知名 | 2022 | [CoW (CLIP on Wheels)](https://arxiv.org/abs/2203.10421) · [專案頁](https://cow.cs.columbia.edu/) | Columbia | 把 CLIP 接上探索策略做 zero-shot 物件導航 | CVPR 2023 | 371 | [158](https://github.com/real-stanford/cow) |
| 主流 | 引用、推薦 | 2025 | [CorrectNav](https://arxiv.org/abs/2508.10416) | PKU | 從錯誤軌跡自動產生自我修正資料反覆後訓練 | AAAI 2026 | 43 | [36](https://github.com/owlet914/CorrectNav) |
| 主流 | 引用、知名 | 2022 | [ZSON](https://arxiv.org/abs/2206.12403) | Georgia Tech | CLIP 目標嵌入讓 ImageNav 策略零樣本找物件 | NeurIPS 2022 | 360 | [110](https://github.com/gunagg/zson) |
| 主流 | 引用、推薦 | 2024 | [CA-Nav](https://arxiv.org/abs/2412.10137) · [專案頁](https://chenkehan21.github.io/CA-Nav-project/) | CASIA / UCAS | 零樣本 VLN-CE 拆成約束感知的子指令完成流程 | TPAMI 2025 | 88 | [85](https://github.com/Chenkehan21/CA-Nav-code) |
| 新興 | HF | 2026 | [Qwen-VLA](https://arxiv.org/abs/2605.30280) | Qwen（Alibaba） | 單一 VLA 同時涵蓋操作與導航；R2R OSR 69.0%、RxR SR 59.6% | arXiv | 65 | 未公開 |
| 新興 | HF | 2026 | [Qwen-RobotNav](https://arxiv.org/abs/2606.18112) | Qwen（Alibaba） | 同一模型支援 2B 到 8B 規模，多任務聯合訓練出可跨任務轉移的空間規劃能力；可零微調轉移到實體機器人 | arXiv | 22 | [197](https://github.com/QwenLM/Qwen-RobotNav) |
| 新興 | 推薦 | 2026 | [HSAN](https://arxiv.org/abs/2606.01565) | HUST / NTU / UCL | 分層語意場景圖加最佳傳輸做連續環境 VLN 規劃 | NeurIPS 2025 | 25 | 未公開 |
| 新興 | 推薦 | 2025 | [MobileVLA-R1](https://arxiv.org/abs/2511.17889) · [專案頁](https://aigeeksgroup.github.io/MobileVLA-R1/) | PKU | CoT 對齊加 GRPO 讓四足 VLA 推理並連續控制 | ECCV 2026 | 16 | [120](https://github.com/AIGeeksGroup/MobileVLA-R1) |
| 新興 | 機構、推薦 | 2026 | [WildOS](https://arxiv.org/abs/2602.19308) · [專案頁](https://leggedrobotics.github.io/wildos/) | NASA JPL / ETH 等 | 戶外長程物件搜尋：稀疏導航圖加基礎模型可通行性推理 | T-FR 2026 | 5 | [162](https://github.com/nasa-jpl/nebula2-wildos) |
| 新興 | 推薦 | 2026 | [HSGM](https://arxiv.org/abs/2606.00095) | ECNU / Bosch / KAUST | 分層語意幾何地圖把 3D 資訊轉成 VLM 可用格式 | CVPR 2026 | 12 | [45](https://github.com/Teacher-Tom/HSGM_public) |
| 新興 | 推薦 | 2025 | [3D Gaussian Map VLN](https://arxiv.org/abs/2605.26500) | Zhejiang | 線上建 3D 高斯地圖並做開放集語意分組 | ICCV 2025 | 13 | [10](https://github.com/Gaozzzz/3D-Gaussian-Map-VLN) |
| 新興 | 推薦 | 2026 | [NaVIDA](https://arxiv.org/abs/2601.18188) | SUSTech / MBZUAI / SpatialTemporal AI | 加入逆動力學監督，學動作如何改變觀測 | arXiv | 11 | [35](https://github.com/waynechu1021/NAVIDA) |
| 新興 | 獲獎、知名 | 2022 | [ViKiNG](https://arxiv.org/abs/2202.11271) · [專案頁](https://sites.google.com/view/viking-release) | UC Berkeley | 學習式局部可通行性加上衛星圖、路網等地理提示做啟發式搜尋，實機走到公里級目標 | RSS 2022 | 118 | 未公開 |
| 新興 | 獲獎、推薦 | 2025 | [VL-Nav](https://arxiv.org/abs/2502.00931) | Univ. at Buffalo / CMU | 神經符號：3D 場景圖與影像記憶輔助 VLM 拆解任務 | IROS 2026 | 11 | 未公開 |
| 新興 | 推薦 | 2021 | [VLN Survey and Taxonomy](https://arxiv.org/abs/2108.11544) | 未確認 | VLN 任務分類與方法綜述 | Neural Computing and Applications 2024 | 93 | 未公開 |
| 新興 | 推薦 | 2026 | [Uncertainty-Aware Gaussian Map](https://arxiv.org/abs/2605.26503) | Zhejiang / Huawei | 語意高斯地圖顯式建模幾何、語意、外觀不確定性 | arXiv | 4 | [10](https://github.com/Gaozzzz/Uncertainty-Aware-VLN) |
| 新興 | 獲獎 | 2026 | [SoftNav](https://arxiv.org/abs/2607.14586) | Shandong / Zhejiang | 3D 場景改以 embedding token 直接注入 VLM，取代轉成文字描述 | IROS 2026 | 1 | 未公開 |
| 新興 | 推薦 | 2026 | [NavOne](https://arxiv.org/abs/2605.06317) | SCUT | 在預建俯視地圖上一步預測整條全域路徑 | arXiv | 0 | 未公開 |

### 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-11 | [Caging Legged VLN](https://arxiv.org/abs/2611.04972) | University of Delaware RPNG | 把高層 VLA 規劃器「關在」物理層外：以機載狀態估計與 SDF 把動作轉成軌跡，Bezier 參數化 MPPI 加離散指數屏障函數（dEBF）給出碰撞避免保證，可換不同 VLM／VLA | 人形與四足實機驗證；未見量化數字 | 未公開 | Humanoids 2026 |
| 2026-11 | [WayTrace](https://arxiv.org/abs/2611.05129) · [專案頁](https://way-trace.github.io) | UC Berkeley、ETH RSL、NVIDIA | 用網路地圖的轉彎導航指令，由現成 VLM 每次下一個原子語言指令（如「向左過馬路」），機載 trace predictor 在影像上畫路徑、RL 策略追蹤，不依賴精準 GNSS | 輪足機器人實機最長 1.37 km、約 1.1 m/s；模擬長程任務違規次數比 point-goal 基線少約 10 倍 | 未公開 | arXiv |
| 2026-10 | [AVALON](https://arxiv.org/abs/2610.21586) | HKU | 只需平面圖與地點線索，以人給的分層拓撲記憶做節點驗證式導航，不建全域 SLAM 圖；人與機器人共同更新記憶 | Unitree Go2 實機 12.81 m 任務 46.4 s（5/5），比 DimOS-Go2 少 40.9% 時間 | 未公開 | arXiv |
| 2026-09 | [AgentVLN](https://arxiv.org/abs/2603.17670) | NUAA | 把 VLM 當大腦、感知與規劃拆成技能庫，3D waypoint 投影回影像當視覺提示，可部署在邊緣平台 |  | [GitHub](https://github.com/Allenxinn/AgentVLN) | ECCV 2026 |
| 2026-09 | [MM-Nav](https://arxiv.org/abs/2510.03142) · [專案頁](https://pku-epic.github.io/MM-Nav-Web/) | PKU / Galbot | 360° 多視角 VLA，向三個分別擅長抵達、穿窄、閃避的 RL 專家學，依各能力表現動態調訓練比例；有實機實驗 |  | 未公開 | ECCV 2026 |

更早的 10 篇見 [topics/vln.md](topics/vln.md)。

## 局部導航與規劃（diffusion / world model / 探索）

### 在解決的問題

- 從感測器直接輸出可行軌跡，取代手調的代價地圖與規劃器參數。
- 泛化到沒見過的環境與機體：靠跨機體資料或大規模模擬訓練。
- 多解行為（岔路要選一邊）用 diffusion 表達；預測動作後果再規劃則走向 world model。
- 安全保證：學習式策略沒有碰撞保證，常另外疊安全濾波器。

### 重要論文（資料日期 2026-11-01）

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 奠基 | 引用、Star、獲獎 | 2024 | [Navigation World Models](https://arxiv.org/abs/2412.03572) · [專案頁](https://www.amirbar.net/nwm/) | Meta | 可控影片生成的導航 world model，用想像軌跡做規劃 | CVPR 2025 | 383 | [704](https://github.com/facebookresearch/nwm) |
| 奠基 | Star、推薦 | 2020 | [FUEL](https://arxiv.org/abs/2010.11561) | HKUST | 增量前沿結構加分層規劃的快速無人機探索 | RA-L 2021 | 418 | [1,513](https://github.com/HKUST-Aerial-Robotics/FUEL) |
| 奠基 | 獲獎 | 2020 | [BADGR](https://arxiv.org/abs/2002.05700) · [專案頁](https://sites.google.com/view/badgr) | UC Berkeley | 從實機自動收集的經驗自監督學習導航，不靠幾何地圖，能學出高草可通行等語意 | RA-L 2021 | 352 | 未公開 |
| 主流 | 引用、Star、獲獎、推薦 | 2023 | [NoMaD](https://arxiv.org/abs/2310.07896) · [專案頁](https://general-navigation-models.github.io/nomad/) | UC Berkeley | diffusion policy 統一有目標導航與無目標探索 | ICRA 2024 | 471 | [1,338](https://github.com/robodhruv/visualnav-transformer) |
| 主流 | 引用、Star | 2023 | [ViNT](https://arxiv.org/abs/2306.14846) · [專案頁](https://visualnav-transformer.github.io) | UC Berkeley | 導航基礎模型：Transformer + 影像目標，可微調到新任務 | CoRL 2023 | 435 | [1,338](https://github.com/robodhruv/visualnav-transformer) |
| 主流 | 引用、Star | 2025 | [NavDP](https://arxiv.org/abs/2505.08712) · [專案頁](https://wzcai99.github.io/navigation-diffusion-policy.github.io) | Shanghai AI Lab | 純模擬訓練 diffusion 導航策略 + 特權資訊引導，zero-shot sim-to-real | ICRA 2026 | 92 | [823](https://github.com/InternRobotics/NavDP) |
| 主流 | 引用、Star、推薦 | 2024 | [NavRL](https://arxiv.org/abs/2409.15634) | CMU | PPO + 安全護盾的動態環境導航（原為無人機，方法可用於地面） | RA-L 2025 | 108 | [1,658](https://github.com/Zhefan-Xu/NavRL) |
| 主流 | 引用、Star | 2022 | [GNM](https://arxiv.org/abs/2210.03370) · [專案頁](https://sites.google.com/view/drive-any-robot) | UC Berkeley | 跨多種機器人資料訓練的通用視覺導航模型 | ICRA 2023 | 319 | [1,338](https://github.com/robodhruv/visualnav-transformer) |
| 主流 | 引用、機構 | 2024 | [CrossFormer](https://arxiv.org/abs/2408.11812) · [專案頁](https://crossformer-model.github.io/) | UC Berkeley / CMU | 單一 Transformer 策略控制手臂、足式、無人機等 | CoRL 2024 | 180 | [285](https://github.com/rail-berkeley/crossformer) |
| 主流 | Star、獲獎 | 2021 | [FAR Planner](https://arxiv.org/abs/2110.09460) | CMU | 未知環境中邊建可視圖邊規劃的快速路徑規劃 | IROS 2022 | 94 | [1,033](https://github.com/MichaelFYang/far_planner) |
| 主流 | Star | 2023 | [ViPlanner](https://arxiv.org/abs/2310.00982) · [專案頁](https://leggedrobotics.github.io/viplanner.github.io/) | ETH | 加入語意的可微分局部規劃，腿式機器人實機 | ICRA 2024 | 115 | [678](https://github.com/leggedrobotics/viplanner) |
| 主流 | 引用 | 2021 | [Embodied AI Survey](https://arxiv.org/abs/2103.04918) | A*STAR / NTU | 從模擬器出發整理具身 AI 研究任務的綜述 | TETCI 2022 | 607 | 未公開 |
| 主流 | 引用、獲獎 | 2024 | [Splat-Nav](https://arxiv.org/abs/2403.02751) · [專案頁](https://chengine.github.io/splatnav) | Stanford | 在 3DGS 地圖用多面體走廊做安全規劃與定位 | T-RO 2025 | 128 | [150](https://github.com/chengine/splatnav) |
| 主流 | 引用、獲獎、機構 | 2025 | [FDM](https://arxiv.org/abs/2504.19322) · [專案頁](https://leggedrobotics.github.io/fdm.github.io/) | ETH / NVIDIA / MPI-IS | 學習感知前向動力學模型評估路徑安全性 | RSS 2025 | 34 | [361](https://github.com/leggedrobotics/fdm) |
| 主流 | 引用 | 2025 | [NaviDiffusor](https://arxiv.org/abs/2504.10003) | Sun Yat-sen | 推論時以成本函數引導擴散模型生成導航路徑 | ICRA 2025 | 49 | [60](https://github.com/SYSU-RoboticsLab/NaviD) |
| 主流 | 引用 | 2024 | [GaussNav](https://arxiv.org/abs/2403.11625) · [專案頁](https://xiaohanlei.github.io/projects/GaussNav/) | USTC | 以 3DGS 地圖取代 BEV 做實例影像目標導航 | TPAMI 2025 | 88 | [220](https://github.com/XiaohanLei/GaussNav) |
| 主流 | 引用 | 2024 | [VLM-Social-Nav](https://arxiv.org/abs/2404.00210) | George Mason / UMD | 用 VLM 打分當社交合規成本項引導導航 | RA-L 2025 | 122 | 未公開 |
| 主流 | 引用 | 2023 | [Social Nav Eval Guidelines](https://arxiv.org/abs/2306.16740) | 未確認 | 社交導航演算法評估的原則、指標與情境建議 | THRI 2025 | 224 | 未公開 |
| 主流 | 引用 | 2025 | [NaviBridger](https://arxiv.org/abs/2504.10041) | Sun Yat-sen | 用先驗分佈取代高斯雜訊的擴散橋導航策略 | CVPR 2025 | 34 | [83](https://github.com/hren20/NaiviBridger) |
| 主流 | 引用 | 2024 | [Cross-Embodiment Nav-Manip](https://arxiv.org/abs/2402.19432) · [專案頁](https://extreme-cross-embodiment.github.io) | Stanford / UC Berkeley / Google DeepMind | 導航與操作資料共同訓練，驗證跨型態正向遷移 | RSS 2024 | 101 | 未公開 |
| 新興 | 獲獎、基準 | 2022 | [TartanDrive](https://arxiv.org/abs/2205.01791) | CMU AirLab | ATV 越野駕駛約 20 萬筆、7 種感測器的資料集，用於學習越野動力學模型 | ICRA 2022 | 110 | [127](https://github.com/castacks/tartan_drive) |
| 新興 | 獲獎 | 2025 | [Realm](https://arxiv.org/abs/2502.15162) | Chongqing / Sichuan / I2R | 未知環境中直接以感測資料建立視線連通約束，多機器人導航時保持彼此可見 | ICRA 2025 | 16 | 未公開 |
| 新興 | 獲獎 | 2025 | [Arm-Pushing Interactive Navigation](https://arxiv.org/abs/2503.01474) | HKUST(GZ) / HKUST | 腿式機械臂學習用手臂推開障礙物，在窄空間開出較短路徑 | IROS 2025 | 14 | 未公開 |
| 新興 | 獲獎 | 2021 | [Legged-Aerial Subterranean Exploration](https://arxiv.org/abs/2111.06482) | NTNU | 四足與無人機協同探索地下環境，以圖式規劃與通訊感知的資料交換分配探索 | ICRA 2022 | 124 | 未公開 |

### 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-10 | [TravSUITE](https://arxiv.org/abs/2610.32130) | CMU / Field AI | 越野高速導航的可通行性系統：高效 voxel mapper 加自監督、含不確定性的 IRL，部署時依風險調整 | 實機導航錯誤減少 80%、穿越速度快 5% | 未公開 | RSS 2026 |
| 2026-10 | [RangeNav](https://arxiv.org/abs/2610.29845) · [專案頁](https://rangenav.github.io/) | ETH RSL / NVIDIA | 只用合成資料預訓練 183k 參數的 LiDAR range-image encoder（重建 + 語意分割 + BEV 預測），凍結後給 RL 導航策略 | 模擬 SR 比僅重建基線平均高 32.03 / 23.73 pp（訓練／OOD 環境）；Unitree B2-W 零樣本實機過人群與工地 | 未公開 | arXiv |
| 2026-10 | [Physical AI for Intralogistics](https://arxiv.org/abs/2610.28432) | Idealworks / NVIDIA | 把 NVIDIA X-Mobility 與 COMPASS 導航策略放進倉儲數位孿生訓練，再用 Cosmos 生成 sim-to-real 變體資料微調，部署在 Jetson AGX Xavier 差速底盤 | 實機四個場景成功率 65.3%（純模擬訓練）→ 91.7%（加 Cosmos 資料），與量產導航堆疊差 8.3 點 | 未公開 | arXiv |
| 2026-10 | [LiteNWM](https://arxiv.org/abs/2610.12368) | Nanjing Univ. / Imperial / Sony AI | 輕量潛空間 world model，可機上跑 | 實機未見場景 SR 43.3%（NoMaD）→ 83.3% | 未公開 | arXiv |
| 2026-09 | [ULVN](https://arxiv.org/abs/2608.06833) · [專案頁](https://hren20.github.io/ulvn-website) | Sun Yat-sen / Insta360 Research | 影像目標導航不需時序影片或深度：從無序影像建圖，用圖上信念傳播定位與規劃子目標；有實機部署 |  | [GitHub](https://github.com/hren20/ulvn) | ECCV 2026 |
| 2026-09 | [A scalar per patch](https://arxiv.org/abs/2606.21216) | NAVER LABS Europe | 大規模實機比較視覺編碼器，發現每個 patch 壓到單一純量仍足以支撐導航，且特徵可對應 affordance | 實體建築 966 個 episode、24 km | 未公開 | ECCV 2026 |
| 2026-09 | [RAE-NWM](https://arxiv.org/abs/2603.09241) | Tsinghua | 導航 world model 改在稠密 DINOv2 特徵空間做時序預測，不用壓縮後的 VAE latent，保留細部結構 |  | [GitHub](https://github.com/20robo/raenwm) | ECCV 2026 |
| 2026-09 | [UniWM](https://arxiv.org/abs/2510.08713) | University of Washington | 單一自迴歸骨幹同時做視覺預想與規劃，讓動作選擇直接依據想像結果，並加入記憶 | 導航成功率最高提升 30% | [GitHub](https://github.com/UWMILab/UniWM) | ECCV 2026 |

更早的 1 篇見 [topics/local-nav.md](topics/local-nav.md)。

## 移動操作感知（導航銜接、抓取、物件遞交）

### 在解決的問題

- 導航到操作的銜接：導航只需粗略位置，抓取需要精確得多的幾何；底盤停在哪裡（base placement）決定手臂搆不搆得到。
- 抓取位姿感知：對沒看過的物件與夾爪，從部分點雲生成無碰撞的 6-DoF 抓取，且要容忍深度雜訊。
- 多相機分工：機身或頭部相機看全局，腕部相機看接觸區，目標要能在相機間接手、被遮擋時不跟丟。
- 共用場景表示：同一份地圖要同時回答「在哪裡」與「怎麼操作」，並隨物件被移動、門被打開而更新。

### 重要論文（資料日期 2026-11-01）

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 主流 | 引用、Star、獲獎 | 2022 | [AnyGrasp](https://arxiv.org/abs/2212.08333) · [專案頁](https://graspnet.net/anygrasp.html) | SJTU | 以真實感知資料與解析標籤做稠密監督，輸出 7-DoF 抓取並可跨幀追蹤，對深度雜訊穩健；實機料堆抓取 93.3% | T-RO 2023 | 561 | [1,050](https://github.com/graspnet/anygrasp_sdk) |
| 主流 | 引用、Star、基準 | 2023 | [HomeRobot](https://arxiv.org/abs/2306.11565) | Georgia Tech / Meta FAIR / CMU / SFU | 定義開放詞彙移動操作（OVMM）benchmark，含模擬與實機；基線實機只有 20%，定位整合難度 | CoRL 2023 | 174 | [1,249](https://github.com/facebookresearch/home-robot) |
| 主流 | 引用、Star | 2025 | [GraspGen](https://arxiv.org/abs/2507.13097) · [專案頁](https://graspgen.github.io) | NVIDIA | 物件點雲輸入的擴散抓取生成器，判別器改用生成器自身輸出訓練；實機整體 81.3% | ICRA 2026 | 69 | [619](https://github.com/NVlabs/GraspGen) |
| 主流 | 引用、Star | 2021 | [Contact-GraspNet](https://arxiv.org/abs/2103.14127) | NVIDIA / DLR / TUM | 把抓取錨定在點雲接觸點，6-DoF 降為 4-DoF，直接由深度圖生成；結構化雜亂場景成功率超過 90% | ICRA 2021 | 596 | [544](https://github.com/NVlabs/contact_graspnet) |
| 主流 | 引用 | 2024 | [MoMa-LLM](https://arxiv.org/abs/2403.08605) · [專案頁](http://moma-llm.cs.uni-freiburg.de) | Freiburg / Toyota Motor Europe | 邊探索邊更新開放詞彙場景圖，LLM 在物件中心動作空間上規劃，可開門開櫃做互動式找物 | RA-L 2024 | 144 | [112](https://github.com/robot-learning-freiburg/MoMa-LLM) |
| 主流 | Star | 2024 | [OK-Robot](https://arxiv.org/abs/2401.12202) · [專案頁](https://ok-robot.github.io) | NYU / AI at Meta | 把現成開放知識模型串成 pick-and-drop 並拆解失敗原因；10 個真實住家 58.5%，整理後 82.4% | RSS 2024 | 53 | [617](https://github.com/ok-robot/ok-robot) |
| 新興 | 機構 | 2026 | [GraspGen-X](https://arxiv.org/abs/2606.00998) | NVIDIA / Princeton | 以掃掠體積編碼夾爪並條件化擴散模型，對沒看過的夾爪零樣本抓取；實機整體 79.0%，優於 GraspGen 與 AnyGrasp | CVPR 2026 | 12 | [286](https://github.com/NVlabs/GraspGenX) |
| 新興 | 獲獎 | 2025 | [MomaGraph](https://arxiv.org/abs/2512.16909) · [專案頁](https://HybridRobotics.github.io/MomaGraph/) | UC Berkeley / Maryland / Toronto | 把空間、功能關係與零件層統一進依任務生成的場景圖；benchmark 準確率 71.6%，實機多步任務整體 70% | ICLR 2026 | 13 | [68](https://github.com/HybridRobotics/MomaGraph) |
| 新興 | 機構 | 2026 | [MoMa-SG](https://arxiv.org/abs/2602.16356) · [專案頁](https://momasg.cs.uni-freiburg.de) | Freiburg / ETH / Bonn | 從 RGB-D 互動序列一次估出轉動與滑動關節，建語意加運動學場景圖；HSR 與 Spot 開關物件成功率皆超過 80%，失敗多為夾取 | CoRL 2026 | 13 | [1](https://github.com/robot-learning-freiburg/MoMa-SG) |

### 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-10 | [FOUND-IT++](https://arxiv.org/abs/2610.23622) | MIT SPARK / Samsung Research America | 基礎模型驅動的階層場景圖在 Jetson Thor 上機，只用單目未校正 RGB（VGGT-Ω 建圖、SAM 3 分割）跑完找物、抓取與歸位 | 10 次任務：導航到物件 100%（76/76）、抓取 50%（9/18）、放置 94%（17/18）；抓取失敗歸因於缺主動深度回饋與策略過於簡單 | [GitHub](https://github.com/MIT-SPARK/FOUND-IT) | arXiv |
| 2026-09 | [REAL](https://arxiv.org/abs/2607.13653) | SJTU / Shanghai AI Lab 等 | 移除模擬器的 oracle 感知 API、只留實體可得的場景先驗，加上模擬使用者，訓練會探索與追問的移動操作 agent | 實機 60 episodes 端到端 78.3%；REAL-Bench 互動任務 56.9% | [GitHub](https://github.com/InternRobotics/REAL) | ECCV 2026 |

更早的 3 篇見 [topics/mobile-manip.md](topics/mobile-manip.md)。

## SLAM 與定位

### 在解決的問題

- 退化場景：長廊、隧道、空曠處 LiDAR 或視覺特徵不足。
- 多感測器緊耦合：LiDAR、IMU、相機融合。
- 學習式前端：用 DROID、MASt3R、VGGT 等取代手工特徵，處理無紋理、免校正相機。
- 稠密且寫實的地圖：NeRF／3DGS SLAM。
- 大尺度、長期：回環、地點辨識、多機器人、場景隨時間變化。

### 重要論文（資料日期 2026-11-01）

#### 視覺與慣性里程計、SLAM

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 奠基 | Star、獲獎 | 2020 | [ORB-SLAM3](https://arxiv.org/abs/2007.11898) | Zaragoza | 視覺／視覺慣性／多地圖 SLAM 的標準基線 | T-RO 2021 | 4,840 | [9,210](https://github.com/UZ-SLAMLab/ORB_SLAM3) |
| 奠基 | 引用、Star | 2024 | [MASt3R-SLAM](https://arxiv.org/abs/2412.12392) · [專案頁](https://edexheim.github.io/mast3r-slam/) | Imperial | 以 MASt3R 3D 重建先驗做即時稠密單眼 SLAM | CVPR 2025 | 334 | [3,234](https://github.com/rmurai0610/MASt3R-SLAM) |
| 奠基 | 引用、Star | 2021 | [DROID-SLAM](https://arxiv.org/abs/2108.10869) | Princeton | 可微分 BA 的深度學習視覺 SLAM | NeurIPS 2021 | 1,303 | [2,720](https://github.com/princeton-vl/DROID-SLAM) |
| 奠基 | 引用、Star | 2025 | [VGGT-SLAM](https://arxiv.org/abs/2505.12549) | MIT SPARK | 用 VGGT 子地圖 + SL(4) 流形優化的 feed-forward SLAM | NeurIPS 2025 | 191 | [1,172](https://github.com/MIT-SPARK/VGGT-SLAM) |
| 奠基 | 引用、Star | 2025 | [VGGT-Long](https://arxiv.org/abs/2507.16443) | Nankai / Nanjing Univ. | 分塊、迴環、對齊讓 VGGT 擴展到公里級序列 | ICRA 2026 | 155 | [910](https://github.com/DengKaiCQ/VGGT-Long) |
| 奠基 | 獲獎 | 2020 | [CodeVIO](https://arxiv.org/abs/2012.10133) | Zhejiang / Delaware | 把可最佳化的稠密深度 code 緊耦合進 VIO，同時輸出狀態估計與稠密深度 | ICRA 2021 | 59 | 未公開 |
| 主流 | 引用、Star、獲獎 | 2024 | [MegaSaM](https://arxiv.org/abs/2412.04463) · [專案頁](https://mega-sam.github.io/) | Google DeepMind / UC Berkeley / Univ. of Michigan | 動態影片也能穩定估計相機與深度的 SLAM 系統 | CVPR 2025 | 276 | [1,371](https://github.com/mega-sam/mega-sam) |
| 主流 | 引用、Star、獲獎 | 2024 | [AirSLAM](https://arxiv.org/abs/2408.03520) · [專案頁](https://sairlab.org/airslam/) | NTU / Univ. at Buffalo 等 | 學習式點線特徵搭配傳統後端的抗光照視覺 SLAM | T-RO 2025 | 125 | [1,215](https://github.com/sair-lab/AirSLAM) |
| 主流 | 引用、Star、獲獎、知名 | 2021 | [GVINS](https://arxiv.org/abs/2103.07899) | HKUST | GNSS 原始量測緊耦合視覺慣性的無漂移狀態估測 | T-RO 2022 | 394 | [1,168](https://github.com/HKUST-Aerial-Robotics/GVINS) |
| 主流 | 引用、Star、知名 | 2022 | [DPVO](https://arxiv.org/abs/2208.04726) | Princeton | 稀疏 patch 的深度視覺里程計，比 DROID 輕量 | NeurIPS 2023 | 336 | [1,146](https://github.com/princeton-vl/DPVO) |
| 新興 | 獲獎 | 2026 | [KISS-IMU](https://arxiv.org/abs/2603.06205) · [專案頁](https://sparolab.github.io/research/kiss_imu) | Inha University | 不需真值的自監督慣性里程計，以運動平衡學習與不確定性感知推論提升泛化 | ICRA 2026 | 2 | 未公開 |

#### LiDAR、雷達與多感測器融合

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 奠基 | 引用、Star、獲獎 | 2021 | [FAST-LIO2](https://arxiv.org/abs/2107.06829) | HKU MaRS | 直接點雲配準 + ikd-tree 的快速 LiDAR 慣性里程計 | T-RO 2022 | 1,948 | [5,327](https://github.com/hku-mars/FAST_LIO) |
| 奠基 | 獲獎 | 2020 | [Multi-Modal Landmark LVIO](https://arxiv.org/abs/2011.06838) | Oxford DRS | 從 LiDAR 抽線與平面基元，與視覺、慣性在同一因子圖緊耦合做里程計 | RA-L 2021 | 122 | 未公開 |
| 主流 | 引用、Star、獲獎、推薦 | 2024 | [FAST-LIVO2](https://arxiv.org/abs/2408.14035) | HKU MaRS | LiDAR-慣性-視覺直接法緊耦合里程計 | T-RO 2025 | 297 | [4,825](https://github.com/hku-mars/FAST-LIVO2) |
| 主流 | 引用、Star | 2022 | [KISS-ICP](https://arxiv.org/abs/2209.15397) | Bonn | 極簡、免調參的 point-to-point ICP LiDAR 里程計 | RA-L 2023 | 625 | [2,365](https://github.com/PRBonn/kiss-icp) |
| 主流 | 引用、Star | 2021 | [R3LIVE](https://arxiv.org/abs/2109.07982) | HKU MaRS | LiDAR-慣性-視覺緊耦合，即時彩色地圖 | ICRA 2022 | 434 | [2,484](https://github.com/hku-mars/r3live) |
| 主流 | 引用、Star | 2021 | [LVI-SAM](https://arxiv.org/abs/2104.10831) | MIT / Stevens | 因子圖緊耦合 LiDAR、視覺與慣性的里程計 | ICRA 2021 | 580 | [1,894](https://github.com/TixiaoShan/LVI-SAM) |
| 主流 | 引用、Star | 2022 | [Faster-LIO](https://doi.org/10.1109/LRA.2022.3152830) | HKU / Idriverplus 等 | 以平行稀疏增量體素取代 ikd-tree，LIO 更快 | RA-L 2022 | 433 | [1,652](https://github.com/gaoxiang12/faster-lio) |
| 主流 | 引用、Star | 2023 | [Point-LIO](https://doi.org/10.1002/aisy.202200459) | HKU MaRS | 逐點更新的高頻寬 LIO，可承受劇烈運動與 IMU 飽和 | Advanced Intelligent Systems 2023 | 281 | [1,372](https://github.com/hku-mars/Point-LIO) |
| 主流 | 引用、Star、知名 | 2021 | [F-LOAM](https://arxiv.org/abs/2107.00822) | NTU | 兩階段失真補償取代迭代的快速 LiDAR 里程計 | IROS 2021 | 407 | [1,145](https://github.com/wh200720041/floam) |
| 主流 | Star、獲獎、知名 | 2021 | [CT-ICP](https://arxiv.org/abs/2109.12979) | MINES ParisTech / Kitware | 每幀以起訖兩個位姿連續插值處理掃描畸變，加上回環偵測組成完整 LiDAR SLAM | ICRA 2022 | 299 | [908](https://github.com/jedeschaud/ct_icp) |

#### NeRF／3DGS 稠密 SLAM

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 奠基 | 引用、Star | 2023 | [SplaTAM](https://arxiv.org/abs/2312.02126) · [專案頁](https://spla-tam.github.io/) | CMU | 3D Gaussian Splatting 的 RGB-D SLAM | CVPR 2024 | 771 | [2,216](https://github.com/spla-tam/SplaTAM) |
| 奠基 | 引用、Star | 2023 | [Gaussian Splatting SLAM](https://arxiv.org/abs/2312.06741) · [專案頁](https://rmurai.co.uk/projects/GaussianSplattingSLAM/) | Imperial | 單眼即時 3DGS SLAM | CVPR 2024 | 761 | [2,189](https://github.com/muskie82/MonoGS) |
| 主流 | 引用、Star | 2021 | [NICE-SLAM](https://arxiv.org/abs/2112.12130) · [專案頁](https://pengsongyou.github.io/nice-slam) | ETH / Zhejiang | 階層式神經隱式表示的稠密 SLAM | CVPR 2022 | 1,167 | [1,601](https://github.com/cvg/nice-slam) |
| 主流 | 引用、Star | 2025 | [WildGS-SLAM](https://arxiv.org/abs/2504.03886) · [專案頁](https://wildgs-slam.github.io/) | ETH / Microsoft / Stanford | DINOv2 不確定度圖剔除動態物的單目 3DGS SLAM | CVPR 2025 | 101 | [661](https://github.com/GradientSpaces/WildGS-SLAM) |
| 主流 | 引用、Star | 2023 | [Gaussian-SLAM](https://arxiv.org/abs/2312.10070) · [專案頁](https://vladimiryugay.github.io/gaussian_slam) | Univ. of Amsterdam | 子地圖組織 3D Gaussian 的可擴展寫實 RGB-D SLAM | arXiv | 283 | [1,187](https://github.com/VladimirYugay/Gaussian-SLAM) |
| 主流 | 引用、Star | 2024 | [SGS-SLAM](https://arxiv.org/abs/2402.03246) | DUT / Univ. of Tokyo / Columbia 等 | 多通道優化外觀幾何語意的 Gaussian 語意 SLAM | ECCV 2024 | 206 | [758](https://github.com/ShuhongLL/SGS-SLAM) |
| 主流 | 引用、知名 | 2023 | [GS-SLAM](https://arxiv.org/abs/2311.11700) · [專案頁](https://gs-slam.github.io/) | Shanghai AI Lab / HKUST / Fudan 等 | 首個用 3D Gaussian 表示的稠密 RGB-D SLAM | CVPR 2024 | 583 | 未公開 |
| 主流 | 引用、知名 | 2023 | [Co-SLAM](https://arxiv.org/abs/2304.14377) · [專案頁](https://hengyiwang.github.io/projects/CoSLAM) | UCL | 座標編碼與雜湊網格混合表示的神經 RGB-D SLAM | CVPR 2023 | 391 | [475](https://github.com/HengyiWang/Co-SLAM) |
| 主流 | 引用、Star、知名 | 2023 | [Photo-SLAM](https://arxiv.org/abs/2311.16728) · [專案頁](https://huajianup.github.io/research/Photo-SLAM/) | HKUST / SYSU | 特徵點定位搭配超原語 Gaussian 的即時寫實建圖 | CVPR 2024 | 298 | [780](https://github.com/HuajianUP/Photo-SLAM) |
| 主流 | 引用、知名 | 2021 | [iMAP](https://arxiv.org/abs/2103.12352) | Imperial | 首次以單一 MLP 作為即時 RGB-D SLAM 的地圖 | ICCV 2021 | 954 | 未公開 |
| 主流 | 引用、知名 | 2023 | [Point-SLAM](https://arxiv.org/abs/2304.04278) | ETH / KU Leuven / Univ. of Amsterdam | 依資訊密度動態佈點的神經點雲稠密 SLAM | ICCV 2023 | 328 | [486](https://github.com/eriksandstroem/Point-SLAM) |

#### 地點辨識與重定位

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 主流 | 引用、Star、知名 | 2023 | [AnyLoc](https://arxiv.org/abs/2308.00688) · [專案頁](https://anyloc.github.io/) | CMU / IIIT | 用基礎模型特徵做通用視覺地點辨識 | RA-L 2024 | 327 | [647](https://github.com/AnyLoc/AnyLoc) |
| 主流 | 引用、Star、知名 | 2021 | [Patch-NetVLAD](https://arxiv.org/abs/2103.01486) | QUT | 從 NetVLAD 殘差取多尺度局部描述子做地點辨識重排序 | CVPR 2021 | 503 | [600](https://github.com/QVPR/Patch-NetVLAD) |
| 主流 | 引用、知名 | 2023 | [MixVPR](https://arxiv.org/abs/2303.02190) | Laval | 以 MLP 特徵混合聚合全域描述子的視覺地點辨識 | WACV 2023 | 325 | [338](https://github.com/amaralibey/MixVPR) |
| 主流 | 引用、知名 | 2023 | [SALAD](https://arxiv.org/abs/2311.15937) | Zaragoza | 以最佳傳輸與 dustbin 重構 NetVLAD 聚合 | CVPR 2024 | 266 | [386](https://github.com/serizba/salad) |
| 主流 | 引用、獲獎、機構、知名 | 2021 | [Scan Context++](https://arxiv.org/abs/2109.13494) | KAIST / NAVER LABS / SNU | 對旋轉與橫向位移穩健的 LiDAR 結構地點描述子 | T-RO 2022 | 360 | [347](https://github.com/gisbi-kim/scancontext_tro) |

#### 點雲配準

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 主流 | 引用、Star、知名 | 2022 | [GeoTransformer](https://arxiv.org/abs/2202.06688) | NUDT / TUM 等 | 以超點間的幾何結構編碼做無關鍵點匹配，低重疊配準不需 RANSAC 也很穩 | CVPR 2022 | 529 | [985](https://github.com/qinzheng93/GeoTransformer) |

#### 多機器人與長期地圖

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 主流 | 引用、Star、機構 | 2021 | [Kimera](https://arxiv.org/abs/2101.06894) | MIT SPARK | 從度量語意 SLAM 建出分層 3D 動態場景圖 | IJRR 2021 | 417 | [2,142](https://github.com/MIT-SPARK/Kimera) |
| 主流 | 引用、獲獎、知名 | 2021 | [Kimera-Multi](https://arxiv.org/abs/2106.14386) | MIT SPARK | 多機器人分散式度量-語意 SLAM | T-RO 2022 | 357 | [417](https://github.com/MIT-SPARK/Kimera-Multi) |

#### 資料集、綜述與工具

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 主流 | 引用、Star、獲獎 | 2024 | [NeRF/3DGS SLAM Survey](https://arxiv.org/abs/2402.13255) | Bologna / ETH / Univ. of Amsterdam 等 | NeRF 與 3DGS 在 SLAM 應用的綜述 | T-RO 2026 | 145 | [2,157](https://github.com/doongli/awesome-implicit-nerf-slam) |
| 主流 | 引用、Star、基準 | 2021 | [M2DGR](https://arxiv.org/abs/2112.13659) | SJTU | 地面機器人多感測器多場景 SLAM 資料集 | RA-L 2022 | 321 | [1,222](https://github.com/SJTU-ViSYS/M2DGR) |
| 主流 | 引用、推薦 | 2025 | [LiDAR-IMU-Camera Fusion SLAM Review](https://doi.org/10.1007/s10462-025-11187-w) | 未確認 | LiDAR、IMU、相機融合 SLAM 的系統性綜述 | Artificial Intelligence Review 2025 | 78 | 未公開 |
| 主流 | 引用、基準 | 2024 | [MCD](https://arxiv.org/abs/2403.11496) | NTU / KTH 等 | 跨歐亞三校園多感測器且含語意標註的資料集 | CVPR 2024 | 100 | 未公開 |
| 新興 | 獲獎、推薦 | 2024 | [BAE](https://arxiv.org/abs/2409.12190) · [專案頁](https://pypose.org/bae/) | Univ. at Buffalo / Georgia Tech / Purdue 等 | PyTorch eager 模式下的 GPU 稀疏 BA 函式庫 | T-RO 2026 | 9 | [379](https://github.com/pypose/bae) |
| 新興 | 獲獎、基準 | 2021 | [VIODE](https://arxiv.org/abs/2102.05965) | EPFL / Tokyo | 模擬無人機在漸增動態物體場景中的 VIO 資料集，專測動態環境穩健度 | RA-L 2021 | 63 | 未公開 |

### 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-11 | [PadLoc](https://arxiv.org/abs/2611.05172) | HTW Berlin | 免訓練的平面圖定位後端：用主要牆向產生少量位姿候選、以遮罩 NCC 比對自由空間，再用移動位姿高斯混合貝氏濾波，取代稠密 (x,y,θ) 網格，狀態大小不隨軌跡增長 | Bonn LiLocBench 比 UnLoc 的 SR@1m 高 23–32 pp（輪式里程計）；Hilti-Trimble 純相機魚眼 5 條序列中 3 條 online SR@2m 0.90–0.98 | [GitHub](https://github.com/mbookhahn/padloc) | WACV 2027 |
| 2026-10 | [Line-Augmented cuVSLAM](https://arxiv.org/abs/2610.20958) | Analog Devices、NVIDIA | 在 NVIDIA cuVSLAM 加線特徵（Plücker 參數化、點線殘差進 Gauss-Newton 位姿解與滑窗 BA），點特徵稀少時自動加重線的權重，針對倉庫等低紋理場景 | RGB-D：TUM Freiburg3 22 條序列 ATE 降 38.5%，Replica 8 條降 30.1% | 未公開 | arXiv |
| 2026-09 | [UniSim-SLAM](https://arxiv.org/abs/2608.01706) · [專案頁](https://vision3d-lab.github.io/unisim-slam/) | UNIST | 前端兩視角追蹤、後端多視角子地圖優化，以統一的 Sim(3) 約束接合不同視角組合的 feed-forward 預測 | 未校正設定下 TUM RGB-D 軌跡誤差降 38.5%、7-Scenes 降 45.9% | [GitHub](https://github.com/vision3d-lab/UniSim-SLAM) | ECCV 2026 |
| 2026-09 | [Register Any Point](https://arxiv.org/abs/2512.01850) | Bonn / Stanford / RWTH Aachen | 把點雲配準當條件生成：用流場把雜訊點直接送到配準後的場景，不做對應匹配與位姿圖 |  | [GitHub](https://github.com/PRBonn/RAP) | ECCV 2026 |
| 2026-09 | [Scal3R](https://arxiv.org/abs/2609.04201) · [專案頁](https://linjohnss.github.io/scal3r/) | NYCU / NVIDIA | 凍結 CUT3R、STream3R 骨幹，只加約 1% 參數的位姿 token 對多個過去關鍵幀並行查相對位姿，再以線上位姿圖與回環融合，長影片不再累積漂移 | KITTI 平均 ATE 比線上基線降 60% 以上；回環示範 ATE 49.8 m → 6.4 m | [GitHub](https://github.com/NVlabs/scal3r) | ECCV 2026 |
| 2026-09 | [FFVO](https://arxiv.org/abs/2609.13733) | Waymo / UW | feed-forward 位姿解碼器做長距離 VO |  | 未公開 | arXiv |

更早的 6 篇見 [topics/slam.md](topics/slam.md)。

## 3D 場景重建（feed-forward、SfM、3DGS／NeRF）

### 在解決的問題

- feed-forward 重建：不跑 SfM 優化，一次前向得到相機與幾何；挑戰在大規模與串流輸入。
- 傳統 SfM 的速度與穩健度：全域最佳化、位姿圖初始化。
- 3D 表示：3DGS 取代 NeRF，可即時渲染；表面品質與無位姿輸入仍在改進。
- 動態場景：同時重建幾何、運動與相機。

### 重要論文（資料日期 2026-11-01）

#### feed-forward 重建

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 奠基 | 引用、Star、HF、獲獎 | 2025 | [VGGT](https://arxiv.org/abs/2503.11651) · [專案頁](https://vgg-t.github.io/) | Oxford VGG / Meta | 單次前向同時估相機、深度、點圖、追蹤 | CVPR 2025 | 2,132 | [14,587](https://github.com/facebookresearch/vggt) |
| 奠基 | Star、HF、推薦 | 2026 | [LingBot-Map](https://arxiv.org/abs/2604.14141) · [專案頁](https://technology.robbyant.com/lingbot-map) | Robbyant (Ant Group) | 借鏡 SLAM 設計錨點與軌跡記憶的串流重建 | ECCV 2026 | 54 | [18,510](https://github.com/robbyant/lingbot-map) |
| 奠基 | 引用、Star | 2023 | [DUSt3R](https://arxiv.org/abs/2312.14132) | Naver Labs | 免相機參數直接回歸 pointmap 的 3D 重建 | CVPR 2024 | 2,114 | [7,361](https://github.com/naver/dust3r) |
| 奠基 | 引用、Star、HF、獲獎 | 2025 | [SAM 3D](https://arxiv.org/abs/2511.16624) · [專案頁](https://ai.meta.com/sam3d/) | Meta | 單張自然影像重建物體幾何、紋理與擺放 | arXiv | 332 | [7,619](https://github.com/facebookresearch/sam-3d-objects) |
| 奠基 | 引用、Star | 2025 | [CUT3R](https://arxiv.org/abs/2501.12387) · [專案頁](https://cut3r.github.io/) | UC Berkeley / Google | 持續狀態更新的串流 3D 重建 | CVPR 2025 | 666 | [1,515](https://github.com/CUT3R/CUT3R) |
| 奠基 | 引用、Star | 2024 | [MASt3R](https://arxiv.org/abs/2406.09756) | Naver Labs | DUSt3R 加特徵匹配頭，提升匹配與定位 | ECCV 2024 | 1,300 | [3,151](https://github.com/naver/mast3r) |
| 奠基 | 引用、Star | 2025 | [MapAnything](https://arxiv.org/abs/2509.13414) · [專案頁](https://map-anything.github.io/) | Meta / CMU | 可接受多種輸入（內參、位姿、深度）的通用 feed-forward 重建 | 3DV 2026 | 402 | [3,868](https://github.com/facebookresearch/map-anything) |
| 奠基 | 引用、Star | 2025 | [Fast3R](https://arxiv.org/abs/2501.13928) · [專案頁](https://fast3r-3d.github.io/) | Meta / Univ. of Michigan | 單次前向處理上千張影像，免兩兩配對 | CVPR 2025 | 459 | [1,593](https://github.com/facebookresearch/fast3r) |
| 奠基 | 引用、Star、HF | 2025 | [π³](https://arxiv.org/abs/2507.13347) · [專案頁](https://yyfz.github.io/pi3/) | Shanghai AI Lab 等 | 無參考視角的置換等變 feed-forward 重建 | arXiv | 388 | [2,234](https://github.com/yyfz/Pi3) |
| 奠基 | 引用、Star | 2025 | [FLARE](https://arxiv.org/abs/2502.12138) · [專案頁](https://zhanghe3z.github.io/FLARE/) | Zhejiang / Ant Group / Oxford 等 | 先估相機再推幾何與外觀的級聯 feed-forward 模型 | CVPR 2025 | 217 | [731](https://github.com/ant-research/FLARE) |
| 奠基 | 引用、Star | 2025 | [StreamVGGT](https://arxiv.org/abs/2507.11539) · [專案頁](https://wzzheng.net/StreamVGGT/) | Tsinghua | 因果注意力與快取把 VGGT 改成串流 4D 重建 | arXiv | 188 | [990](https://github.com/wzzheng/StreamVGGT) |
| 奠基 | 引用 | 2025 | [MUSt3R](https://arxiv.org/abs/2503.01661) | Naver Labs Europe | DUSt3R 擴展為多視角對稱架構並加入記憶機制 | CVPR 2025 | 180 | [345](https://github.com/naver/must3r) |
| 奠基 | 引用、Star | 2025 | [TTT3R](https://arxiv.org/abs/2509.26645) · [專案頁](https://rover-xingyu.github.io/TTT3R/) | Zhejiang / Westlake / Univ. of Tübingen | 把記憶更新視為測試期訓練，免重訓延長序列長度 | ICLR 2026 | 151 | [740](https://github.com/Inception3D/TTT3R) |
| 主流 | 引用、Star、獲獎、知名 | 2024 | [Spann3R](https://arxiv.org/abs/2408.16061) · [專案頁](https://hengyiwang.github.io/projects/spanner) | UCL | 以空間記憶逐幀增量回歸 pointmap，免全域對齊 | 3DV 2025 | 319 | [1,146](https://github.com/hengyiwang/spann3r) |
| 主流 | 引用、Star、知名 | 2024 | [MV-DUSt3R+](https://arxiv.org/abs/2412.06974) · [專案頁](https://mv-dust3rp.github.io/) | Meta / UIUC | 單階段多視角同時重建，免兩兩配對後全域對齊 | CVPR 2025 | 174 | [607](https://github.com/facebookresearch/mvdust3r) |
| 主流 | Star、HF | 2026 | [LoGeR](https://arxiv.org/abs/2603.03269) · [專案頁](https://loger-project.github.io/) | Google DeepMind / UC Berkeley | 混合記憶架構，訓練只用 128 幀，推論可到上萬幀；KITTI ATE 降超過 74% | arXiv | 42 | [630](https://github.com/Junyi42/LoGeR) |
| 新興 | HF | 2026 | [InfiniteVGGT](https://arxiv.org/abs/2601.02281) | SJTU | 讓 VGGT 類模型處理無限長串流，並提出約 1 萬幀的 Long3D benchmark | arXiv | 61 | [395](https://github.com/AutoLab-SAI-SJTU/InfiniteVGGT) |
| 新興 | 機構、推薦 | 2026 | [ScaRF-SLAM](https://arxiv.org/abs/2606.00307) | Oxford ORI / Georgia Tech | 定位交給傳統視覺 SLAM，feed-forward 幾何模型只做深度與稠密重建，再以跨幀與子地圖的尺度一致性最佳化串起來；單目、雙目、多相機、有無 IMU 都能套 | RA-L 2026 | 3 | [294](https://github.com/ori-drs/ScaRF-SLAM) |
| 新興 | 獲獎 | 2026 | [VGGT-Ω](https://arxiv.org/abs/2605.15195) · [專案頁](https://vggt-omega.github.io/) | Meta / Oxford VGG | 驗證 feed-forward 重建品質隨模型與資料規模可預測地提升，並擴展到動態場景 | CVPR 2026 | 18 | 未公開 |
| 新興 | 獲獎 | 2026 | [LSRM](https://arxiv.org/abs/2604.05182) | Meta Reality Labs | 大幅擴大 transformer 上下文中的物件與影像 token，讓 feed-forward 物件重建逼近稠密最佳化品質 | ECCV 2026 | 3 | 未公開 |

#### SfM 與相機位姿

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 主流 | 引用、Star、獲獎、知名 | 2024 | [MASt3R-SfM](https://arxiv.org/abs/2409.19152) | Naver Labs Europe | 以 MASt3R 匹配與檢索建構免調參的全整合 SfM | 3DV 2025 | 208 | [3,151](https://github.com/naver/mast3r) |
| 主流 | 引用、Star、知名 | 2023 | [VGGSfM](https://arxiv.org/abs/2312.04563) · [專案頁](https://vggsfm.github.io/) | Oxford VGG / Meta | 全流程可微分的深度 SfM，取代增量式配對與三角化 | CVPR 2024 | 293 | [1,430](https://github.com/facebookresearch/vggsfm) |
| 主流 | 引用、Star、獲獎、知名 | 2021 | [PixSfM](https://arxiv.org/abs/2108.08291) · [專案頁](https://psarlin.com/pixsfm/) | ETH / Microsoft | 以深度特徵度量精修關鍵點與 BA，提升 SfM 精度 | ICCV 2021 | 310 | [1,496](https://github.com/cvg/pixel-perfect-sfm) |
| 新興 | 獲獎 | 2026 | [Global-Aware Edge Prioritization](https://arxiv.org/abs/2602.21963) | CTU Prague / ETH | SfM 位姿圖初始化時考慮全域一致性來挑選候選邊，取代只看 kNN 檢索 | CVPR 2026 | 1 | 未公開 |

#### 3DGS／NeRF 表示與渲染

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 奠基 | 引用、Star、HF | 2023 | [3D Gaussian Splatting](https://arxiv.org/abs/2308.04079) · [專案頁](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/) | Inria | 即時可微分高斯渲染，取代 NeRF 成為主流 3D 表示 | SIGGRAPH 2023 | 11,224 | [24,384](https://github.com/graphdeco-inria/gaussian-splatting) |
| 奠基 | 引用、Star | 2022 | [Instant-NGP](https://arxiv.org/abs/2201.05989) · [專案頁](https://nvlabs.github.io/instant-ngp) | NVIDIA | 多解析度雜湊編碼，秒級訓練 NeRF | SIGGRAPH 2022 | 6,560 | [17,585](https://github.com/NVlabs/instant-ngp) |
| 奠基 | 引用、Star | 2023 | [Nerfstudio](https://arxiv.org/abs/2302.04264) · [專案頁](https://nerf.studio) | UC Berkeley | 模組化 NeRF／3DGS 重建框架 | SIGGRAPH 2023 | 1,085 | [12,137](https://github.com/nerfstudio-project/nerfstudio) |
| 奠基 | 引用、Star、HF | 2024 | [2D Gaussian Splatting](https://arxiv.org/abs/2403.17888) · [專案頁](https://surfsplatting.github.io) | ShanghaiTech / Tübingen | 幾何準確的表面重建，可輸出網格 | SIGGRAPH 2024 | 1,795 | [3,327](https://github.com/hbb1/2d-gaussian-splatting) |
| 奠基 | 引用、Star | 2024 | [gsplat](https://arxiv.org/abs/2409.06765) · [專案頁](https://docs.gsplat.studio/) | UC Berkeley | 開源 CUDA 高斯潑濺函式庫 | JMLR 2025 | 426 | [5,854](https://github.com/nerfstudio-project/gsplat) |
| 奠基 | 引用、Star、HF | 2023 | [SuGaR](https://arxiv.org/abs/2311.12775) · [專案頁](https://anttwo.github.io/sugar/) | ENPC | 從 3DGS 抽出可編輯網格 | CVPR 2024 | 1,026 | [3,552](https://github.com/Anttwo/SuGaR) |
| 奠基 | 引用、Star、HF | 2025 | [AnySplat](https://arxiv.org/abs/2505.23716) · [專案頁](https://city-super.github.io/anysplat/) | USTC / Shanghai AI Lab | 無校正多視角一次前向輸出 3DGS 與相機參數 | SIGGRAPH Asia 2025 | 316 | [961](https://github.com/InternRobotics/AnySplat) |
| 奠基 | 引用、Star | 2024 | [MVSplat](https://arxiv.org/abs/2403.14627) · [專案頁](https://donydchen.github.io/mvsplat) | Monash / ETH / Univ. of Tübingen 等 | 以平面掃描代價體定位高斯中心的稀疏視角 3DGS | ECCV 2024 | 695 | [1,319](https://github.com/donydchen/mvsplat) |
| 奠基 | 引用、Star、獲獎 | 2023 | [pixelSplat](https://arxiv.org/abs/2312.12337) · [專案頁](https://dcharatan.github.io/pixelsplat) | MIT / Simon Fraser / Univ. of Toronto | 由兩張影像前向預測 3D 高斯的通用重建 | CVPR 2024 | 889 | [1,284](https://github.com/dcharatan/pixelsplat) |
| 奠基 | 引用、Star | 2024 | [DepthSplat](https://arxiv.org/abs/2410.13862) · [專案頁](https://haofeixu.github.io/depthsplat/) | ETH / Univ. of Tübingen / Univ. of Bonn 等 | 單眼深度特徵與前向 3DGS 結合並互相增益 | CVPR 2025 | 366 | [1,275](https://github.com/cvg/depthsplat) |
| 奠基 | 引用 | 2024 | [PGSR](https://arxiv.org/abs/2406.06521) · [專案頁](https://zju3dv.github.io/pgsr/) | Zhejiang / SenseTime | 把高斯壓成平面並加多視角幾何約束，3DGS 得到高精度表面且保留快速訓練 | TVCG 2024 | 463 | 未公開 |
| 主流 | 引用、Star、獲獎、知名 | 2024 | [NoPoSplat](https://arxiv.org/abs/2410.24207) · [專案頁](https://noposplat.github.io/) | ETH / NVIDIA / Microsoft 等 | 免相機位姿、直接在標準空間預測 3D 高斯 | ICLR 2025 | 310 | [1,004](https://github.com/cvg/NoPoSplat) |

#### 動態與 4D

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 奠基 | 引用、Star、HF | 2024 | [MonST3R](https://arxiv.org/abs/2410.03825) · [專案頁](https://monst3r-project.github.io/) | UC Berkeley / Google DeepMind / Stability AI 等 | 逐幀 pointmap 推廣到動態場景的幾何估計 | ICLR 2025 | 512 | [1,392](https://github.com/Junyi42/monst3r) |
| 主流 | 引用、HF、獲獎、推薦 | 2025 | [D4RT](https://arxiv.org/abs/2512.08924) · [專案頁](https://d4rt-paper.github.io/) | Google DeepMind / UCL / Oxford | 單一 transformer 從影片同時推深度、時空對應與相機參數，用逐點查詢取代逐幀稠密解碼，動態場景 4D 重建又快又輕 | CVPR 2026 | 72 | 未公開 |
| 新興 | 推薦 | 2026 | [Foundation4D](https://arxiv.org/abs/2610.30340) · [專案頁](https://research.nvidia.com/labs/sil/projects/foundation4d/) | NVIDIA | 多相機行車影片共用時空分解注意力骨幹，一次 feed-forward 出深度、3D 偵測、語意 occupancy 與高斯重建，預測的幾何與軌跡可當無 LiDAR 的 NuRec 重建先驗 | NVIDIA Research、arXiv | 0 | 未公開 |

#### 表面、TSDF 與點雲補全

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 主流 | 引用、Star、獲獎、知名 | 2021 | [NeuralRecon](https://arxiv.org/abs/2104.00681) · [專案頁](https://zju3dv.github.io/neuralrecon/) | Zhejiang / SenseTime | 直接增量重建 TSDF，不再逐幀估深度後融合 | CVPR 2021 | 407 | [2,288](https://github.com/zju3dv/NeuralRecon) |
| 主流 | 引用、Star、知名 | 2021 | [PoinTr](https://arxiv.org/abs/2108.08839) | Tsinghua | 把點雲補全改成集合到集合的翻譯，以幾何感知 transformer 由殘缺點雲生成缺漏部分 | ICCV 2021 | 697 | [870](https://github.com/yuxumin/PoinTr) |
| 主流 | Star、推薦 | 2023 | [nvblox](https://arxiv.org/abs/2311.00626) · [專案頁](https://nvidia-isaac.github.io/nvblox) | NVIDIA / ETH | GPU 加速的增量式 TSDF／ESDF 建圖，即時產出供路徑規劃用的距離場 | ICRA 2024 | 101 | [1,336](https://github.com/nvidia-isaac/nvblox) |
| 主流 | 引用、Star、推薦 | 2023 | [NKSR](https://arxiv.org/abs/2305.19590) · [專案頁](https://research.nvidia.com/labs/toronto-ai/NKSR/) | NVIDIA | 以神經核場從帶雜訊的大規模點雲重建表面，稀疏體素加梯度擬合，可一次處理整個場景並泛化到未見過的資料 | CVPR 2023 | 157 | [1,005](https://github.com/nv-tlabs/nksr) |

#### 資料集與綜述

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 奠基 | 引用、基準 | 2023 | [ScanNet++](https://arxiv.org/abs/2308.11417) · [專案頁](https://cy94.github.io/scannetpp/) | TUM | 雷射掃描＋單眼相機＋iPhone 的高精度室內資料集 | ICCV 2023 | 994 | [415](https://github.com/scannetpp/scannetpp) |
| 奠基 | 引用 | 2024 | [3DGS Survey](https://arxiv.org/abs/2401.03890) | Zhejiang | 系統整理 3DGS 技術並附統一效能比較 | ACM Computing Surveys | 393 | [115](https://github.com/guikunchen/Awesome3DGS) |
| 主流 | 引用、Star、獲獎、基準 | 2021 | [CO3D](https://arxiv.org/abs/2109.00512) | Meta / UCL | 大規模真實物件多視角影片資料集，含相機位姿與點雲，用於類別級 3D 重建評估 | ICCV 2021 | 807 | [1,186](https://github.com/facebookresearch/co3d) |

### 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-10 | [ACE-Zero + PGO](https://arxiv.org/abs/2610.35501) · [專案頁](https://eldentse.github.io/visual_localization_pgo_public/) | dConstruct Robotics / NUS | 在 ACE-Zero 上加 pose graph optimization，由預測的 scene coordinate 取相對位姿，並以對極與光流一致性估信心來抑制錯誤修正 |  | 未公開 | CVPR 2026 |
| 2026-09 | [FILT3R](https://arxiv.org/abs/2603.18493) | KAIST | 串流重建的狀態更新改用 token 空間的 Kalman 式增益，免訓練即可外掛，改善長序列穩定度 |  | [GitHub](https://github.com/jinotter3/FILT3R) | ECCV 2026 |
| 2026-09 | [OVGGT](https://arxiv.org/abs/2603.05959) · [專案頁](https://vaisr.github.io/OVGGT/) | NTU / NTUST | 壓縮 KV cache 並保護座標關鍵 token，免訓練把串流 VGGT 的記憶體與計算量壓到固定額度 |  | [GitHub](https://github.com/VAISR/OVGGT) | ECCV 2026 |

更早的 5 篇見 [topics/reconstruction.md](topics/reconstruction.md)。

## 深度估計與 occupancy

### 在解決的問題

- 單眼公制深度：要有絕對尺度，且相機內參常未知。
- 雙目深度的零樣本泛化。
- 透明、反光表面讓深度感測器失效。
- occupancy：多源自自駕，室內與開放詞彙版本正在補上。

### 重要論文（資料日期 2026-11-01）

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 奠基 | 引用、Star、HF | 2024 | [Depth Anything V2](https://arxiv.org/abs/2406.09414) · [專案頁](https://depth-anything-v2.github.io) | HKU / TikTok | 以合成資料標註提升細節的深度模型 | NeurIPS 2024 | 2,472 | [9,079](https://github.com/DepthAnything/Depth-Anything-V2) |
| 奠基 | 引用、Star、HF | 2024 | [Depth Anything](https://arxiv.org/abs/2401.10891) · [專案頁](https://depth-anything.github.io) | HKU / TikTok | 大規模未標註資料訓練的單眼深度基礎模型 | CVPR 2024 | 2,292 | [8,247](https://github.com/LiheYoung/Depth-Anything) |
| 奠基 | 引用、Star、HF、推薦 | 2025 | [Depth Anything 3](https://arxiv.org/abs/2511.10647) · [專案頁](https://depth-anything-3.github.io/) | ByteDance Seed | 任意視角數的深度與位姿估計 | arXiv | 905 | [6,611](https://github.com/ByteDance-Seed/Depth-Anything-3) |
| 奠基 | 引用、Star、HF | 2024 | [Depth Pro](https://arxiv.org/abs/2410.02073) | Apple | 免相機內參、一秒內輸出銳利邊緣的公制深度 | ICLR 2025 | 624 | [5,773](https://github.com/apple/ml-depth-pro) |
| 奠基 | 引用、Star、獲獎 | 2025 | [FoundationStereo](https://arxiv.org/abs/2501.09898) · [專案頁](https://nvlabs.github.io/FoundationStereo/) | NVIDIA | 零樣本雙目深度基礎模型 | CVPR 2025 | 329 | [2,976](https://github.com/NVlabs/FoundationStereo) |
| 奠基 | 引用、Star | 2021 | [DPT](https://arxiv.org/abs/2103.13413) | Intel | ViT 做稠密預測，後續單眼深度模型的骨幹設計 | ICCV 2021 | 3,246 | [2,330](https://github.com/isl-org/DPT) |
| 奠基 | 引用、Star、HF | 2025 | [Video Depth Anything](https://arxiv.org/abs/2501.12375) · [專案頁](https://videodepthanything.github.io) | ByteDance | 時序頭加一致性損失，超長影片保持深度穩定 | CVPR 2025 | 295 | [2,314](https://github.com/DepthAnything/Video-Depth-Anything) |
| 奠基 | 引用、Star | 2023 | [ZoeDepth](https://arxiv.org/abs/2302.12288) | Intel | 相對深度預訓練 + 公制深度頭，零樣本公制深度 | arXiv | 1,080 | [2,834](https://github.com/isl-org/ZoeDepth) |
| 奠基 | 引用、Star | 2024 | [Metric3D v2](https://arxiv.org/abs/2404.15506) · [專案頁](https://JUGGHM.github.io/Metric3Dv2) | HKUST 等 | 零樣本公制深度與法向量 | TPAMI 2024 | 605 | [2,337](https://github.com/YvanYin/Metric3D) |
| 奠基 | 引用、Star | 2024 | [MoGe](https://arxiv.org/abs/2410.19115) · [專案頁](https://wangrc.site/MoGePage/) | Microsoft | 單張影像估計仿射不變點雲 | CVPR 2025 | 388 | [3,115](https://github.com/microsoft/MoGe) |
| 奠基 | 引用、Star | 2025 | [UniDepthV2](https://arxiv.org/abs/2502.20110) · [專案頁](https://lpiccinelli-eth.github.io/pub/unidepth/) | ETH / Toyota Motor Europe / INSAIT | 同時估計相機與深度的通用公制深度簡化版 | TPAMI 2026 | 243 | [1,277](https://github.com/lpiccinelli-eth/unidepth) |
| 奠基 | 引用、Star | 2024 | [UniDepth](https://arxiv.org/abs/2403.18913) · [專案頁](https://lpiccinelli-eth.github.io/pub/unidepth/) | ETH | 同時估計相機內參的通用公制深度 | CVPR 2024 | 541 | [1,277](https://github.com/lpiccinelli-eth/UniDepth) |
| 奠基 | 引用、Star | 2024 | [GeoWizard](https://arxiv.org/abs/2403.12013) · [專案頁](https://fuxiao0719.github.io/projects/geowizard/) | CUHK / Univ. of Adelaide / HKUST 等 | 用擴散先驗聯合估計深度與法向量 | ECCV 2024 | 358 | [942](https://github.com/fuxiao0719/GeoWizard) |
| 奠基 | 獲獎 | 2020 | [LeReS](https://arxiv.org/abs/2012.09365) | Adelaide / Adobe | 先估到尺度與平移未定的深度，再以點雲網路補回位移與焦距，從單張影像還原 3D 場景形狀 | CVPR 2021 | 347 | 未公開 |
| 主流 | 引用、Star | 2023 | [MiDaS v3.1](https://arxiv.org/abs/2307.14460) | Intel | 多種 Transformer 骨幹的相對深度模型庫 | arXiv | 304 | [5,413](https://github.com/isl-org/MiDaS) |
| 主流 | 引用、Star | 2023 | [Marigold](https://arxiv.org/abs/2312.02145) · [專案頁](https://marigoldmonodepth.github.io) | ETH | 把影像 diffusion 模型轉成深度估計器 | CVPR 2024 | 532 | [3,246](https://github.com/prs-eth/Marigold) |
| 主流 | 引用、Star | 2023 | [Metric3D](https://arxiv.org/abs/2307.10984) · [專案頁](https://jugghm.github.io/Metric3Dv2/) | DJI / Tencent / Zhejiang 等 | 正規相機空間轉換解決焦距歧義的零樣本公制深度 | ICCV 2023 | 532 | [2,337](https://github.com/YvanYin/Metric3D) |
| 主流 | 引用、Star、HF | 2024 | [DepthCrafter](https://arxiv.org/abs/2409.02095) · [專案頁](https://depthcrafter.github.io) | Tencent / HKUST | 以影片擴散模型生成時序一致的長影片深度 | CVPR 2025 | 255 | [1,597](https://github.com/Tencent/DepthCrafter) |
| 主流 | 引用、Star | 2025 | [Fast-FoundationStereo](https://arxiv.org/abs/2512.11130) · [專案頁](https://nvlabs.github.io/Fast-FoundationStereo/) | NVIDIA | 蒸餾加架構搜尋，首次即時零樣本雙目匹配 | arXiv | 56 | [1,576](https://github.com/NVlabs/Fast-FoundationStereo) |
| 主流 | 引用、Star | 2021 | [RAFT-Stereo](https://arxiv.org/abs/2109.07547) | Princeton | 迭代更新的雙目深度估計 | 3DV 2021 | 773 | [1,138](https://github.com/princeton-vl/RAFT-Stereo) |
| 主流 | Star、HF、推薦 | 2026 | [LingBot-Depth](https://arxiv.org/abs/2601.17895) · [專案頁](https://technology.robbyant.com/lingbot-depth) | Robbyant (Ant Group) | 把感測器深度缺陷當遮罩訊號做深度補全 | ECCV 2026 | 41 | [1,689](https://github.com/Robbyant/lingbot-depth) |
| 主流 | 引用、Star | 2023 | [IGEV-Stereo](https://arxiv.org/abs/2303.06615) | HUST | 以幾何編碼體積取代全配對相關性做迭代雙目匹配 | CVPR 2023 | 454 | [693](https://github.com/gangweix/IGEV) |
| 主流 | 引用、Star | 2025 | [UniK3D](https://arxiv.org/abs/2503.16591) · [專案頁](https://lpiccinelli-eth.github.io/pub/unik3d/) | ETH / Toyota Motor Europe / INSAIT | 以球面光線表示支援任意相機模型的單眼 3D | CVPR 2025 | 83 | [763](https://github.com/lpiccinelli-eth/UniK3D) |
| 主流 | 引用、Star | 2022 | [UniMatch](https://arxiv.org/abs/2211.05783) · [專案頁](https://haofeixu.github.io/unimatch) | ETH / Univ. of Tübingen / Univ. of Sydney 等 | 光流、雙目、深度統一為稠密匹配的單一模型 | TPAMI 2023 | 446 | [1,387](https://github.com/autonomousvision/unimatch) |
| 主流 | 引用 | 2025 | [DEFOM-Stereo](https://arxiv.org/abs/2501.09466) · [專案頁](https://insta360-research-team.github.io/DEFOM-Stereo/) | Insta360 / CUHK-Shenzhen | 把深度基礎模型嵌入遞迴雙目匹配框架 | CVPR 2025 | 106 | [306](https://github.com/Insta360-Research-Team/DEFOM-Stereo) |
| 主流 | 引用、Star | 2024 | [PromptDA](https://arxiv.org/abs/2412.14015) · [專案頁](https://PromptDA.github.io/) | Zhejiang / ByteDance Seed / SJTU 等 | 以低解析 LiDAR 當提示，輸出 4K 公制深度 | CVPR 2025 | 116 | [1,181](https://github.com/DepthAnything/PromptDA) |
| 主流 | 引用、Star、知名 | 2022 | [CREStereo](https://arxiv.org/abs/2203.11483) | Megvii / Tencent 等 | 階層式遞迴網路搭配自適應相關，適用實拍雙目 | CVPR 2022 | 444 | [640](https://github.com/megvii-research/CREStereo) |
| 主流 | 引用、推薦 | 2025 | [MVSAnywhere](https://arxiv.org/abs/2503.22430) · [專案頁](https://nianticlabs.github.io/mvsanywhere/) | Niantic / Univ. of Zaragoza / UCL 等 | 可變視角數並自估深度範圍的零樣本多視角立體 | CVPR 2025 | 37 | [345](https://github.com/nianticlabs/mvsanywhere) |
| 新興 | 獲獎 | 2026 | [Indoor Open-Vocab Occupancy](https://arxiv.org/abs/2602.22667) | HKUST(GZ) | 針對室內密集幾何與細粒度語意，從單目影像預測開放詞彙 3D occupancy | CVPR 2026 | 10 | 未公開 |
| 新興 | 獲獎、推薦 | 2026 | [GlassRecon](https://arxiv.org/abs/2604.18336) · [專案頁](https://jarvisyjw.github.io/GlassRecon/) | HKUST / HKU / SUSTech / ASTRI | 免訓練，用局部 RANSAC 把深度基礎模型對齊到感測器深度，避開玻璃區的錯誤量測並補回公制尺度 | IROS 2026 | 2 | [12](https://github.com/jarvisyjw/GlassRecon) |
| 新興 | 獲獎 | 2026 | [SeeGroup](https://arxiv.org/abs/2605.28735) | Princeton | 讓模型自行決定點的分層方式，估計透明表面與其後物體的多層深度 | CVPR 2026 | 1 | 未公開 |

### 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-09 | [ZipDepth](https://arxiv.org/abs/2607.08771) · [專案頁](https://zipdepth.github.io/) | University of Bologna | 可重參數化編解碼器加多領域基礎模型蒸餾，讓輕量單目深度也有 zero-shot 泛化，可上嵌入式裝置 | 6.1M 參數 | [GitHub](https://github.com/fabiotosi92/ZipDepth) | ECCV 2026 |
| 2026-09 | [WAFT-Stereo](https://arxiv.org/abs/2603.24836) | Princeton | 證明雙目匹配不一定要 cost volume，只用 warping 就能達到領先表現 | ETH3D zero-shot 誤差降 81%；比競品快 1.8–6.7 倍 | [GitHub](https://github.com/princeton-vl/WAFT-Stereo) | ECCV 2026 |
| 2026-09 | [MetricAnything](https://arxiv.org/abs/2601.22054) · [專案頁](https://metric-anything.github.io/metric-anything-io/) | Li Auto | 隨機遮罩深度圖形成稀疏度量提示，讓模型能從雜訊大、來源不一的 3D 資料學度量深度 |  | [GitHub](https://github.com/metric-anything/metric-anything) | ECCV 2026 |
| 2026-09 | [MobileOcc](https://arxiv.org/abs/2511.16949) · [專案頁](https://autonomousrobots.nl/paper_websites/mobileocc) | TU Delft | 行人密集環境下給移動機器人用的語意 occupancy 資料集，用 mesh 優化標註可變形的人體佔據 |  | 未公開 | ECCV 2026 |
| 2026-09 | [Monocular Depth Estimation: Progress and Opportunities](https://arxiv.org/abs/2609.01172) | HKU | 單眼深度綜述 |  | [GitHub](https://github.com/CVMI-Lab/Depth_Survey) | arXiv |

更早的 1 篇見 [topics/perception-3d.md](topics/perception-3d.md)。

## 語意地圖與場景圖

### 在解決的問題

- 開放詞彙：不限定類別，能用任意語言查物件與區域。
- 可擴展：稠密特徵地圖太大，改用物件／房間／樓層的階層場景圖壓縮。
- 即時、增量：邊走邊建，並處理場景變動。
- 當成 LLM／VLM 規劃的介面。

### 重要論文（資料日期 2026-11-01）

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 奠基 | 引用、Star、推薦 | 2023 | [ConceptGraphs](https://arxiv.org/abs/2309.16650) · [專案頁](https://concept-graphs.github.io/) | Toronto / MIT | 用 2D 基礎模型建開放詞彙 3D 場景圖，支援 LLM 規劃 | ICRA 2024 | 715 | [980](https://github.com/concept-graphs/concept-graphs) |
| 奠基 | 引用、Star | 2023 | [LERF](https://arxiv.org/abs/2303.09553) · [專案頁](https://lerf.io) | UC Berkeley | 把 CLIP 特徵嵌進 NeRF 做語言查詢 | ICCV 2023 | 780 | [734](https://github.com/kerrj/lerf) |
| 奠基 | 引用、Star | 2023 | [LangSplat](https://arxiv.org/abs/2312.16084) · [專案頁](https://langsplat.github.io/) | Tsinghua / Harvard | 以 3D Gaussian 承載 SAM 階層語意的 CLIP 語言場 | CVPR 2024 | 617 | [1,096](https://github.com/minghanqin/LangSplat) |
| 奠基 | 引用、Star | 2024 | [HOV-SG](https://arxiv.org/abs/2403.17846) · [專案頁](http://hovsg.github.io/) | Freiburg | 樓層／房間／物件階層開放詞彙場景圖，跨樓層語言導航 | RSS 2024 | 374 | [561](https://github.com/hovsg/HOV-SG) |
| 主流 | 引用、Star、推薦 | 2022 | [VLMaps](https://arxiv.org/abs/2210.05714) · [專案頁](https://vlmaps.github.io) | Freiburg / Google | 把 VLM 特徵融合進 3D 地圖，可用語言查空間位置 | ICRA 2023 | 730 | [731](https://github.com/vlmaps/vlmaps) |
| 主流 | 引用、Star | 2022 | [Hydra](https://arxiv.org/abs/2201.13360) | MIT SPARK | 即時建立階層式 3D 場景圖（物件／房間／樓層） | RSS 2022 | 410 | [1,189](https://github.com/MIT-SPARK/Hydra) |
| 主流 | 引用、獲獎 | 2023 | [SayPlan](https://arxiv.org/abs/2307.06135) · [專案頁](https://sayplan.github.io) | QUT / Univ. of Adelaide | LLM 在 3D 場景圖上語意搜尋做大尺度任務規劃 | CoRL 2023 | 554 | 未公開 |
| 主流 | 引用 | 2023 | [ConceptFusion](https://arxiv.org/abs/2302.07241) · [專案頁](https://concept-fusion.github.io) | MIT / Toronto | 把基礎模型特徵融合成開放集合 3D 地圖 | RSS 2023 | 467 | [248](https://github.com/concept-fusion/concept-fusion) |
| 主流 | 引用、獲獎 | 2021 | [Semantic-NeRF](https://arxiv.org/abs/2103.15875) · [專案頁](https://shuaifengzhi.com/Semantic-NeRF/) | Imperial | NeRF 同時編碼語意，少量標註即可補全場景標籤 | ICCV 2021 | 589 | [462](https://github.com/Harry-Zhi/semantic_nerf) |
| 主流 | 引用 | 2025 | [OpenFunGraph](https://arxiv.org/abs/2503.19199) · [專案頁](https://openfungraph.github.io/) | Tsinghua / ETH / Microsoft 等 | 含功能元件與互動關係的開放詞彙功能性場景圖 | CVPR 2025 | 83 | [60](https://github.com/ZhangCYG/OpenFunGraph) |
| 主流 | 引用 | 2025 | [Dr. Splat](https://arxiv.org/abs/2502.16652) · [專案頁](https://drsplat.github.io/) | POSTECH / KAIST / NVIDIA | 把語言特徵直接登錄到 3D Gaussian 上，不必逐視角渲染特徵，查詢更快 | CVPR 2025 | 76 | [107](https://github.com/kaist-ami/Dr-Splat) |
| 主流 | 引用 | 2024 | [Clio](https://arxiv.org/abs/2404.13696) | MIT SPARK | 依任務決定物件粒度的場景圖（information bottleneck） | RA-L 2024 | 163 | [264](https://github.com/MIT-SPARK/Clio) |
| 主流 | 引用、推薦 | 2024 | [ReMEmbR](https://arxiv.org/abs/2409.13682) · [專案頁](https://nvidia-ai-iot.github.io/remembr/) | NVIDIA / USC / UT Austin | VILA 把機器人影片轉成帶位置與時間的描述存進向量資料庫，LLM 迴圈檢索回答長時間部署中的空間、時間與描述性問題 | ICRA 2025 | 125 | [361](https://github.com/NVIDIA-AI-IOT/remembr) |
| 主流 | 引用 | 2023 | [LEGaussians](https://arxiv.org/abs/2311.18482) · [專案頁](https://buaavrcg.github.io/LEGaussians/) | Beihang | 量化壓縮語言特徵嵌入 3D Gaussian 做開放詞彙查詢 | CVPR 2024 | 274 | [174](https://github.com/buaavrcg/LEGaussians) |
| 主流 | 引用、推薦 | 2024 | [3D-Mem](https://arxiv.org/abs/2411.17735) · [專案頁](https://umass-embodied-agi.github.io/3D-Mem/) | UMass Amherst / CUHK / Columbia 等 | 以多視角快照影像當 3D 場景記憶支援探索與推理 | CVPR 2025 | 126 | [283](https://github.com/UMass-Embodied-AGI/3D-Mem) |
| 主流 | 引用 | 2024 | [Open3DSG](https://arxiv.org/abs/2402.12259) · [專案頁](https://kochsebastian.com/open3dsg) | Bosch / Ulm / TU Vienna | 從點雲預測開放詞彙物件與開放集合關係的場景圖 | CVPR 2024 | 137 | [166](https://github.com/boschresearch/Open3DSG) |
| 主流 | 引用 | 2024 | [Semantic Gaussians](https://arxiv.org/abs/2403.15624) · [專案頁](https://semantic-gaussians.github.io) | BIGAI / Tsinghua | 免訓練將 2D 預訓練模型語意蒸餾到 3D Gaussian | TCSVT 2026 | 106 | [278](https://github.com/sharinka0715/semantic-gaussians) |
| 主流 | 引用、機構 | 2025 | [RayFronts](https://arxiv.org/abs/2504.06994) · [專案頁](https://rayfronts.github.io/) | CMU | 以語意射線前緣同時表示範圍內與超出範圍的語意 | IROS 2025 | 45 | [149](https://github.com/RayFronts/RayFronts) |
| 主流 | 引用 | 2024 | [FMGS](https://arxiv.org/abs/2401.01970) · [專案頁](https://xingxingzuo.github.io/fmgs) | Google | 3DGS 結合多解析度雜湊編碼嵌入基礎模型特徵 | IJCV 2025 | 137 | 未公開 |
| 主流 | 引用 | 2025 | [OpenGS-SLAM](https://arxiv.org/abs/2503.01646) · [專案頁](https://young-bit.github.io/opengs-github.github.io/) | BIT | Gaussian 投票濺射的開放集合物件級語意 SLAM | ICRA 2025 | 32 | [314](https://github.com/YOUNG-bit/open_semantic_slam) |
| 主流 | 引用 | 2024 | [SemGauss-SLAM](https://arxiv.org/abs/2403.07494) | SJTU / Cambridge | 語意特徵嵌入 3D Gaussian 的稠密語意 SLAM | IROS 2025 | 105 | [82](https://github.com/IRMVLab/SemGauss-SLAM) |
| 主流 | 引用 | 2025 | [FunGraph](https://arxiv.org/abs/2503.07909) · [專案頁](https://fungraph.github.io) | Univ. of Stuttgart / Bonn | 偵測可操作部件的功能感知 3D 場景圖 | IROS 2025 | 31 | [20](https://github.com/DennisRotondi/FunGraph) |
| 新興 | 獲獎 | 2025 | [FindAnything](https://arxiv.org/abs/2504.08603) · [專案頁](https://ethz-mrl.github.io/findanything/) | TUM / Imperial | 把視覺語言特徵併入物件中心的體素子地圖，即時、可擴展的開放詞彙探索建圖 | ICRA 2026 | 16 | 未公開 |
| 新興 | 獲獎、推薦 | 2026 | [LT-Mem](https://arxiv.org/abs/2608.19059) · [專案頁](https://lt-mem.github.io/) | DGIST | 多 session SLAM 對齊物件後，依物件變動程度選擇覆寫、保留或多假設，保存跨 session 的物件身分與歷史，可回答「某物去過哪裡」 | IROS 2026 | 0 | [37](https://github.com/yumin1102/LT-Mem) |

### 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-10 | [OASIS](https://arxiv.org/abs/2610.30589) · [專案頁](https://starry-curry-30.github.io/oasis-project) | Beihang Univ. | 以少量穩定語意錨點節點建立線上地圖，每個節點整合語意描述、視覺特徵與幾何，支援開放詞彙檢索並在場景變動後重新定位被移動的物件 |  | [GitHub](https://github.com/starry-curry-30/OASIS) | ACM MM 2026 |
| 2026-10 | [AOV-GS](https://arxiv.org/abs/2610.29374) | MIPT / AIRI | 主動 3D Gaussian 建圖：以 SAM 實例的 CLIP 嵌入新穎度重排候選視角，不需人工標註遮罩 | 同樣 SAM-CLIP 下語言場 mIoU 比純幾何探索高 1.3 pp（Replica 34.6%）、1.8 pp（Matterport3D 23.1%） | [GitHub](https://github.com/OptimusFaber/AOV-GS) | AIST 2026 |
| 2026-10 | [Industrial ReMEmbR](https://arxiv.org/abs/2610.28624) | Idealworks / NVIDIA | 把 ReMEmbR 擴成多機器人共用的時空記憶：機上只上傳嵌入與視覺 token，描述改為查詢時才生成，並把人像遮掉 | NaVQA 首次解析失敗率 20.7% → 13.8%；快取 token 解碼 450 次與原模型輸出一致 | 未公開 | arXiv |
| 2026-09 | [PUF](https://arxiv.org/abs/2607.07170) | Leibniz Hannover / IIT / Bath | 線上 3D 場景圖不再確定性融合，把節點關聯改成機率似然，不需訓練即可外掛到既有方法 |  | [GitHub](https://github.com/yyyyangyi/PUF) | ECCV 2026 |
| 2026-09 | [NoPA](https://arxiv.org/abs/2607.00529) · [專案頁](https://qixun1.github.io/projects/nopa/) | NUS | 線上場景圖的物件從單一高斯改為固定數量粒子，保留幾何細節，並在高相似物件間傳播關係 |  | [GitHub](https://github.com/qixun1/nopa) | ECCV 2026 |
| 2026-09 | [OP3DSG](https://arxiv.org/abs/2606.29786) · [專案頁](https://k2room.github.io/OP3DSG/) | GIST | 開放詞彙場景圖加入物件零件與 affordance 層，並提出 UniGraph3D benchmark；有實際機器人任務驗證 |  | [GitHub](https://github.com/AutoCompSysLab/OP3DSG) | ECCV 2026 |

更早的 1 篇見 [topics/semantic-map.md](topics/semantic-map.md)。

## 3D 偵測與分割（點雲骨幹、3D 偵測、語意／實例分割）

### 在解決的問題

- 點雲骨幹：在大場景上兼顧準確與速度，並靠自監督或 2D 基礎模型蒸餾減少 3D 標註。
- 開放詞彙 3D 偵測與實例分割：3D 標註少，靠 2D 基礎模型（CLIP、SAM）的結果提升到 3D。
- 物件位姿與形狀：從點雲或單張影像估計物件 6D／9D 位姿。

### 重要論文（資料日期 2026-11-01）

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 奠基 | 引用、Star | 2023 | [FoundationPose](https://arxiv.org/abs/2312.08344) · [專案頁](https://nvlabs.github.io/FoundationPose/) | NVIDIA | 單一模型同時支援有 CAD 與只有少量參考影像兩種設定，對未見過的物件做 6D 位姿估計與追蹤 | CVPR 2024 | 904 | [3,667](https://github.com/NVlabs/FoundationPose) |
| 奠基 | 引用、Star、HF | 2023 | [Point Transformer V3](https://arxiv.org/abs/2312.10035) | HKU / Shanghai AI Lab / MIT 等 | 用序列化取代精確鄰域搜尋，換取大感受野與速度，以規模取勝的點雲骨幹 | CVPR 2024 | 1,216 | [1,985](https://github.com/Pointcept/PointTransformerV3) |
| 奠基 | 引用、Star | 2025 | [Sonata](https://arxiv.org/abs/2503.16429) · [專案頁](https://xywu.me/sonata/) | Meta Reality Labs / HKU | 找出自監督點雲模型的幾何捷徑問題並修正，linear probing 即可用於多種 3D 任務 | CVPR 2025 | 164 | [808](https://github.com/facebookresearch/sonata) |
| 奠基 | 引用、Star | 2022 | [PointNeXt](https://arxiv.org/abs/2206.04670) · [專案頁](https://guochengqian.github.io/PointNeXt/) | KAUST / Microsoft | 只改訓練策略與縮放就讓 PointNet++ 追上新架構，提供強而簡單的點雲基線 | NeurIPS 2022 | 1,321 | [1,092](https://github.com/guochengqian/pointnext) |
| 奠基 | 引用、Star | 2024 | [PointMamba](https://arxiv.org/abs/2402.10739) | HUST / Baidu | 以狀態空間模型取代注意力，線性複雜度的點雲分析骨幹 | NeurIPS 2024 | 399 | [550](https://github.com/LMD0311/PointMamba) |
| 奠基 | 引用 | 2021 | [Point-BERT](https://arxiv.org/abs/2111.14819) · [專案頁](https://point-bert.ivg-research.xyz) | Tsinghua / PKU / BAAI | 把 BERT 遮罩建模搬到點雲，以離散 token 做點雲 transformer 預訓練 | CVPR 2022 | 1,256 | 未公開 |
| 主流 | 引用、Star | 2022 | [OpenScene](https://arxiv.org/abs/2211.15654) · [專案頁](https://pengsongyou.github.io/openscene) | ETH / Google | 零樣本開放詞彙 3D 場景理解 | CVPR 2023 | 835 | [857](https://github.com/pengsongyou/openscene) |
| 主流 | 引用、Star | 2022 | [Point-MAE](https://arxiv.org/abs/2203.06604) | PKU / Tencent | 點雲版的遮罩自編碼器，遮掉點塊再重建做自監督預訓練 | ECCV 2022 | 836 | [649](https://github.com/Pang-Yatian/Point-MAE) |
| 主流 | 引用、Star、基準 | 2021 | [ARKitScenes](https://arxiv.org/abs/2111.08897) | Apple | 用 iPad LiDAR 拍的大規模室內 RGB-D 資料集，附高精度雷射掃描與 3D 框 | NeurIPS 2021 Datasets and Benchmarks | 559 | [975](https://github.com/apple/ARKitScenes) |
| 主流 | 引用、Star | 2021 | [3DETR](https://arxiv.org/abs/2109.08141) · [專案頁](https://facebookresearch.github.io/3detr) | Meta FAIR | 純 transformer 編碼解碼器直接輸出 3D 框，不需手工設計的 3D 算子，室內點雲偵測的簡潔基線 | ICCV 2021 | 657 | [718](https://github.com/facebookresearch/3detr) |
| 主流 | 引用、Star | 2023 | [Uni3D](https://arxiv.org/abs/2310.06773) | BAAI / Tsinghua / PKU | 以 2D ViT 初始化並擴到 10 億參數的 3D 表示模型，對齊影像文字特徵做零樣本 3D 辨識 | ICLR 2024 | 298 | [690](https://github.com/baaivision/Uni3D) |
| 主流 | 引用、Star | 2023 | [Superpoint Transformer](https://arxiv.org/abs/2306.08045) | IGN / Univ Gustave Eiffel | 先把點雲分成階層超點再做注意力，大場景語意分割參數少、訓練快 | ICCV 2023 | 173 | [1,067](https://github.com/drprojects/superpoint_transformer) |
| 主流 | 引用 | 2023 | [OpenMask3D](https://arxiv.org/abs/2306.13631) · [專案頁](https://openmask3d.github.io/) | ETH / Microsoft / Google | 多視角融合 CLIP 特徵的零樣本開放詞彙 3D 實例分割 | NeurIPS 2023 | 406 | [273](https://github.com/OpenMask3D/openmask3d) |
| 主流 | 引用 | 2022 | [Point Transformer V2](https://arxiv.org/abs/2210.05666) | HKU 等 | 分組向量注意力與分區池化，降低 Point Transformer 的計算並提升分割表現 | NeurIPS 2022 | 954 | 未公開 |
| 主流 | 引用、Star | 2022 | [Mask3D](https://arxiv.org/abs/2210.03105) · [專案頁](https://jonasschult.github.io/Mask3D/) | RWTH Aachen / ETH / NVIDIA | 以 Transformer 實例查詢直接預測 3D 實例遮罩，不需手工分群 | ICRA 2023 | 492 | [748](https://github.com/JonasSchult/Mask3D) |
| 主流 | 引用、Star、HF | 2025 | [Concerto](https://arxiv.org/abs/2510.23607) · [專案頁](https://pointcept.github.io/Concerto/) | HKU / CUHK / HIT(SZ) | 2D-3D 聯合自監督學習，單用點雲也能喚起與影像一致的空間表示 | NeurIPS 2025 | 50 | [542](https://github.com/Pointcept/Concerto) |
| 主流 | Star、HF | 2026 | [Utonia](https://arxiv.org/abs/2603.03283) · [專案頁](https://pointcept.github.io/Utonia/) | HKU / CUHK / Xiaomi | 用單一編碼器處理不同來源的點雲，朝點雲基礎模型發展，特徵也可供 VLA 與空間推理使用 | ICML 2026 | 35 | [771](https://github.com/Pointcept/Utonia) |
| 主流 | 引用、Star | 2023 | [OneFormer3D](https://arxiv.org/abs/2311.14405) | Samsung Research | 單一 transformer 同時做點雲語意、實例與全景分割 | CVPR 2024 | 212 | [618](https://github.com/oneformer3d/oneformer3d) |
| 主流 | Star、基準 | 2022 | [Omni3D / Cube R-CNN](https://arxiv.org/abs/2207.10660) · [專案頁](https://garrickbrazil.com/omni3d) | Meta AI | 整合室內外多資料集的單張影像 3D 偵測基準，Cube R-CNN 跨相機與場景通用 | CVPR 2023 | 230 | [854](https://github.com/facebookresearch/omni3d) |
| 主流 | Star、獲獎 | 2022 | [EPro-PnP](https://arxiv.org/abs/2203.13254) | Tongji / Alibaba | 把 PnP 輸出改成位姿機率分布，使 2D-3D 對應能端到端學習，用於單目物件位姿估計 | CVPR 2022 | 3 | [1,177](https://github.com/tjiiv-cprg/EPro-PnP) |
| 主流 | 引用 | 2022 | [Stratified Transformer](https://arxiv.org/abs/2203.14508) | HKU / CUHK / SmartMore 等 | 近處密、遠處稀的分層取樣 key，讓點雲分割模型能建模長距離關係 | CVPR 2022 | 432 | [430](https://github.com/dvlab-research/Stratified-Transformer) |
| 主流 | 引用 | 2023 | [CLIP2Scene](https://arxiv.org/abs/2301.04926) | Shanghai AI Lab / HKU 等 | 把 CLIP 知識蒸餾到 3D 點雲網路，標註少或零標註也能做場景語意分割 | CVPR 2023 | 286 | [188](https://github.com/runnanchen/clip2scene) |
| 主流 | 引用 | 2022 | [SoftGroup](https://arxiv.org/abs/2203.01509) | KAIST | 點雲 3D 實例分割，以軟語意分數分群減少語意誤判造成的實例錯誤 | CVPR 2022 | 376 | [462](https://github.com/thangvubk/SoftGroup) |
| 主流 | 引用 | 2025 | [DITR (DINO in the Room)](https://arxiv.org/abs/2503.18944) · [專案頁](https://vision.rwth-aachen.de/ditr) | RWTH Aachen / Bosch | 把 DINOv2 影像特徵投影到點雲注入 3D 分割骨幹，或在無影像時用來蒸餾 | 3DV 2026 | 50 | [116](https://github.com/VisualComputingInstitute/DITR) |
| 主流 | 引用 | 2021 | [DepthContrast](https://arxiv.org/abs/2101.02691) | Meta FAIR / UT Austin | 不限點雲格式的對比式自監督預訓練，單視角深度掃描也能用 | ICCV 2021 | 361 | [275](https://github.com/facebookresearch/DepthContrast) |
| 主流 | 引用 | 2023 | [OctFormer](https://arxiv.org/abs/2305.03045) · [專案頁](https://wang-ps.github.io/octformer) | Peking University | 以八叉樹排序切窗做注意力，複雜度線性，大場景點雲分割與偵測更快 | SIGGRAPH 2023 | 246 | 未公開 |
| 主流 | 引用 | 2022 | [ULIP](https://arxiv.org/abs/2212.05171) | Salesforce / Stanford | 以影像-文字-點雲三模態對比學習，把 CLIP 空間延伸到 3D | CVPR 2023 | 452 | 未公開 |
| 主流 | 引用 | 2023 | [Open3DIS](https://arxiv.org/abs/2312.10671) · [專案頁](https://open3dis.github.io/) | VinAI / UMass Amherst / MIT-IBM Watson AI Lab | 聚合跨幀 2D 實例遮罩補足 3D 開放詞彙實例分割 | CVPR 2024 | 178 | [140](https://github.com/VinAIResearch/Open3DIS) |
| 主流 | 引用、基準 | 2022 | [ScanNet200](https://arxiv.org/abs/2204.07761) · [專案頁](https://rozdavid.github.io/scannet200) | TUM / NVIDIA | 把 ScanNet 擴到 200 類長尾室內語意分割基準，並用 CLIP 文字特徵預訓練點雲特徵改善少見類別 | ECCV 2022 | 340 | [124](https://github.com/RozDavid/LanguageGroundedSemseg) |
| 主流 | 引用 | 2024 | [OA-CNNs](https://arxiv.org/abs/2403.14418) | HKU / CUHK 等 | 讓稀疏 CNN 自適應調整感受野，在點雲分割上追平 transformer 且更快 | CVPR 2024 | 107 | 未公開 |

### 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-10 | [F2G-Pose](https://arxiv.org/abs/2610.31623) · [專案頁](https://jrryzh.github.io/F2G-Pose/) | Fudan Univ. / Shanghai Innovation Institute | 凍結 RADIO 基礎特徵抬升到局部點雲，單次 feed-forward 同時預測類別層級位姿、尺寸與補全形狀 | SOPE、ROPE 達 SOTA（作者自報）；位姿推論 28 FPS | [GitHub](https://github.com/jrryzh/F2G-Pose) | NeurIPS 2026 |
| 2026-09 | [Co-3DGT](https://arxiv.org/abs/2608.19973) | UESTC / SUTD / Hainan | 開放詞彙 3D 偵測在物件發現階段做共同蒸餾，訓練階段用雙重引導降低不準的框與語意的影響 |  | [GitHub](https://github.com/shangboyuan/Co-3DGT) | ECCV 2026 |

## 3D 空間理解（3D grounding、空間推理 VLM、3D-LLM）

### 在解決的問題

- 3D grounding：把「沙發右邊的桌子」這類含空間關係的描述對到 3D 中的特定物件。
- VLM 的空間推理：VLM 多用 2D 圖文訓練，距離、方位、大小常答錯；做法是用 3D 資料合成空間問答，或接上深度、點雲輸入。
- 從影片理解空間：機器人只有連續影像、沒有完整點雲時，要從影片累積對空間的記憶與推理。

### 重要論文（資料日期 2026-11-01）

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 奠基 | 引用、HF | 2024 | [SpatialVLM](https://arxiv.org/abs/2401.12168) · [專案頁](https://spatial-vlm.github.io/) | Google DeepMind / Google Research | 用網路圖片加深度與物件偵測自動合成大規模 3D 空間問答，讓 VLM 能回答距離、大小等定量問題 | CVPR 2024 | 1,172 | 未公開 |
| 奠基 | 引用、Star、HF、基準 | 2024 | [VSI-Bench](https://arxiv.org/abs/2412.14171) · [專案頁](https://vision-x-nyu.github.io/thinking-in-space.github.io/) | NYU / Yale / Stanford | 從室內影片測 MLLM 空間記憶與推理的 benchmark，發現模型會在內部形成局部認知地圖 | CVPR 2025 | 884 | [752](https://github.com/vision-x-nyu/thinking-in-space) |
| 奠基 | 引用、HF | 2025 | [Spatial-MLLM](https://arxiv.org/abs/2505.23747) · [專案頁](https://diankun-wu.github.io/Spatial-MLLM/) | Tsinghua | 在 2D 視覺編碼器旁加 VGGT 幾何編碼器，只用影片就提升 MLLM 的空間推理 | NeurIPS 2025 | 268 | [497](https://github.com/diankun-wu/Spatial-MLLM) |
| 奠基 | 引用、基準 | 2025 | [MMSI-Bench](https://arxiv.org/abs/2505.23764) · [專案頁](https://runsenxu.com/projects/MMSI_Bench) | Shanghai AI Lab / CUHK 等 | 多張影像的空間推理 benchmark，人工出題，最強模型與人類差距仍大 | ICLR 2026 | 233 | [111](https://github.com/OpenRobotLab/MMSI-Bench) |
| 奠基 | 引用 | 2025 | [VLM-3R](https://arxiv.org/abs/2505.20279) · [專案頁](https://vlm-3r.github.io) | UT Austin / UCLA / Meta 等 | 從單眼影片重建 3D 特徵並與指令對齊，讓 VLM 做空間與時間推理 | CVPR 2026 | 200 | [452](https://github.com/VITA-Group/VLM-3R) |
| 奠基 | 引用、Star、HF | 2025 | [Cambrian-S](https://arxiv.org/abs/2511.04670) · [專案頁](https://cambrian-mllm.github.io/) | NYU / Stanford | 從影片做空間超感知：以預測下一幀的驚訝度決定記憶與事件切分，並提出 VSI-SUPER | arXiv | 164 | [572](https://github.com/cambrian-mllm/cambrian-s) |
| 奠基 | 引用、HF | 2025 | [RoboRefer](https://arxiv.org/abs/2506.04308) · [專案頁](https://zhoues.github.io/RoboRefer/) | Beihang / PKU / BAAI | 以 SFT 加 RL 訓練能多步推理的空間指代 VLM，輸出機器人要去或放的點 | NeurIPS 2025 | 177 | [268](https://github.com/Zhoues/RoboRefer) |
| 奠基 | 引用 | 2024 | [SpatialRGPT](https://arxiv.org/abs/2406.01584) · [專案頁](https://www.anjiecheng.me/SpatialRGPT) | UC San Diego / NVIDIA | 以區域提示加深度輸入，讓 VLM 對指定區域做相對方向與距離推理 | NeurIPS 2024 | 454 | [342](https://github.com/AnjieCheng/SpatialRGPT) |
| 奠基 | 引用、Star | 2025 | [GPT4Scene](https://arxiv.org/abs/2501.01428) · [專案頁](https://gpt4scene.github.io/) | HKU / Shanghai AI Lab | 從影片重建鳥瞰圖並在畫面與鳥瞰圖標上一致的物件編號，讓 VLM 建立全域空間關係 | arXiv | 132 | [547](https://github.com/Qi-Zhangyang/GPT4Scene-and-VLN-R1) |
| 奠基 | 引用 | 2025 | [VG LLM](https://arxiv.org/abs/2505.24625) · [專案頁](https://lavi-lab.github.io/VG-LLM/) | CUHK | 在 MLLM 中加 3D 幾何編碼器，直接從影片抽出 3D 先驗，不需點雲或深度 | NeurIPS 2025 | 145 | [261](https://github.com/LaVi-Lab/VG-LLM) |
| 奠基 | 引用 | 2025 | [SPAR](https://arxiv.org/abs/2503.22976) · [專案頁](https://logosroboticsgroup.github.io/SPAR/) | Fudan / Huawei Noah's Ark | 從 3D 掃描自動生成 700 萬筆空間問答（SPAR-7M），只用 2D 輸入就提升 VLM 3D 推理 | NeurIPS 2025 | 153 | [99](https://github.com/fudan-zvg/spar) |
| 奠基 | 引用、HF、基準 | 2025 | [OmniSpatial](https://arxiv.org/abs/2506.03135) · [專案頁](https://qizekun.github.io/omnispatial/) | Tsinghua / PKU / Galbot 等 | 涵蓋動態推理、視角轉換等進階空間推理的 benchmark | ICLR 2026 | 127 | [95](https://github.com/qizekun/OmniSpatial) |
| 奠基 | 基準 | 2019 | [ScanRefer](https://arxiv.org/abs/1912.08830) · [專案頁](https://daveredrum.github.io/ScanRefer/) | TUM / Simon Fraser Univ. | 第一個 RGB-D 掃描上的 3D 語言 grounding 資料集與基線 | ECCV 2020 | 687 | [306](https://github.com/daveredrum/ScanRefer) |
| 主流 | 引用、Star、HF | 2025 | [SpatialLM](https://arxiv.org/abs/2506.07491) · [專案頁](https://manycore-research.github.io/SpatialLM) | Manycore Tech / HKUST | LLM 吃點雲直接輸出牆、門窗與物件 3D 框的結構化場景描述 | NeurIPS 2025 | 98 | [5,114](https://github.com/manycore-research/SpatialLM) |
| 主流 | 引用、基準 | 2025 | [MM-Spatial](https://arxiv.org/abs/2503.13111) | Apple | 提出室內 3D 空間問答資料集 CA-VQA，訓練能估深度與 3D 位置的 MLLM | ICCV 2025 | 101 | [450](https://github.com/apple/ml-cubifyanything) |
| 主流 | 引用 | 2023 | [LEO](https://arxiv.org/abs/2311.12871) · [專案頁](https://embodied-generalist.github.io/) | BIGAI 等 | 在 3D 場景中同時做描述、問答、導航與操作的具身通用模型 | ICML 2024 | 473 | [492](https://github.com/embodied-generalist/embodied-generalist) |
| 主流 | 引用、HF | 2025 | [VST](https://arxiv.org/abs/2511.05491) · [專案頁](https://yangr116.github.io/vst_project/) | ByteDance Seed | 以空間感知與空間推理兩段資料漸進訓練 VLM，不改架構提升空間能力 | arXiv | 95 | [215](https://github.com/Yangr116/VST) |
| 主流 | 引用、HF | 2024 | [LLaVA-3D](https://arxiv.org/abs/2409.18125) · [專案頁](https://zcmax.github.io/projects/LLaVA-3D/) | HKU / Shanghai AI Lab | 在 LLaVA 的 2D patch 上加 3D 位置編碼，沿用 2D 預訓練權重快速獲得 3D 理解 | ICCV 2025 | 203 | [392](https://github.com/ZCMax/LLaVA-3D) |
| 主流 | Star、HF | 2026 | [RynnBrain](https://arxiv.org/abs/2602.14979) · [專案頁](https://alibaba-damo-academy.github.io/RynnBrain.github.io/) | Alibaba DAMO | 開源的具身基礎模型，著重物理情境下的推理與規劃，可再訓練成不同機器人任務的骨幹 | arXiv | 42 | [900](https://github.com/alibaba-damo-academy/RynnBrain) |
| 主流 | 引用、獲獎、基準 | 2024 | [RoboSpatial](https://arxiv.org/abs/2411.16537) · [專案頁](https://chanh.ee/RoboSpatial) | Ohio State / NVIDIA | 機器人視角的大規模空間理解資料集（含參考座標系與可放置位置），訓練 2D/3D VLM | CVPR 2025 | 225 | [153](https://github.com/NVlabs/RoboSpatial) |
| 主流 | 引用、獲獎 | 2023 | [PointLLM](https://arxiv.org/abs/2308.16911) · [專案頁](https://runsenxu.com/projects/PointLLM) | Shanghai AI Lab / CUHK | 把彩色物件點雲接進 LLM，依指令描述、問答物件 | ECCV 2024 | 467 | 未公開 |
| 主流 | 引用 | 2025 | [SpatialReasoner](https://arxiv.org/abs/2504.20024) · [專案頁](https://spatial-reasoner.github.io) | Johns Hopkins 等 | 讓 VLM 推理時先寫出明確的 3D 位置與方向，再據此回答 | NeurIPS 2025 | 83 | [45](https://github.com/johnson111788/SpatialReasoner) |
| 主流 | 引用、HF、基準 | 2024 | [SceneVerse](https://arxiv.org/abs/2401.09340) · [專案頁](https://scene-verse.github.io) | BIGAI | 約 6.8 萬個室內場景、數百萬句 3D 語言標註，用來預訓練 3D grounding 模型 | ECCV 2024 | 179 | [291](https://github.com/scene-verse/SceneVerse) |
| 主流 | 引用、Star、基準 | 2023 | [EmbodiedScan](https://arxiv.org/abs/2312.16170) · [專案頁](https://tai-wang.github.io/embodiedscan/) | Shanghai AI Lab 等 | 以機器人第一人稱 RGB-D 視角標註的 3D 偵測、occupancy 與 grounding 基準 | CVPR 2024 | 214 | [680](https://github.com/InternRobotics/EmbodiedScan) |
| 主流 | 引用 | 2024 | [Video-3D LLM](https://arxiv.org/abs/2412.00493) | CUHK | 把 3D 場景當影片，在影片特徵加 3D 座標編碼做 3D 理解 | CVPR 2025 | 181 | [226](https://github.com/LaVi-Lab/Video-3D-LLM) |
| 主流 | Star、HF | 2023 | [3D-LLM](https://arxiv.org/abs/2307.12981) · [專案頁](https://vis-www.cs.umass.edu/3dllm/) | UCLA / UMass Amherst / MIT-IBM Watson AI Lab | 把多視角 2D 特徵提升成 3D 特徵輸入 LLM，一個模型做 3D 問答、描述、grounding | NeurIPS 2023 | 0 | [1,218](https://github.com/UMass-Embodied-AGI/3D-LLM) |
| 主流 | 引用、知名 | 2023 | [Chat-Scene](https://arxiv.org/abs/2312.08168) | Zhejiang / Shanghai AI Lab / ByteDance | 給場景中每個物件一個識別碼 token，讓 LLM 用識別碼指涉物件做 grounding 與問答 | NeurIPS 2024 | 247 | [222](https://github.com/ZzZZCHS/Chat-Scene) |
| 主流 | 引用、基準 | 2021 | [ScanQA](https://arxiv.org/abs/2112.10482) | Kyoto Univ. / RIKEN AIP | 提出 3D 問答任務與資料集：在室內掃描上回答空間問題並定位相關物件 | CVPR 2022 | 518 | [165](https://github.com/ATR-DBI/ScanQA) |
| 主流 | 引用、知名 | 2023 | [LLM-Grounder](https://arxiv.org/abs/2309.12311) · [專案頁](https://chat-with-nerf.github.io/) | Univ. of Michigan | LLM 當代理拆解查詢並呼叫工具做 3D 視覺定位 | ICRA 2024 | 208 | [322](https://github.com/sled-group/chat-with-nerf) |
| 主流 | 引用、基準 | 2022 | [VSR](https://arxiv.org/abs/2205.00363) | Univ. of Cambridge | 圖文配對形式的空間關係 benchmark，顯示 VLM 在方位關係上遠落後人類 | TACL 2023 | 406 | [150](https://github.com/cambridgeltl/visual-spatial-reasoning) |
| 主流 | 引用、基準 | 2023 | [Multi3DRefer](https://arxiv.org/abs/2309.05251) · [專案頁](https://3dlg-hcvc.github.io/multi3drefer/) | Simon Fraser Univ. | 3D grounding 擴充為一句描述可對應零到多個物件，附資料集與基線 | ICCV 2023 | 214 | [99](https://github.com/3dlg-hcvc/M3DRef-CLIP) |
| 主流 | 引用、HF、基準 | 2025 | [OST-Bench](https://arxiv.org/abs/2507.07984) · [專案頁](https://rbler1234.github.io/OSTBench.github.io/) | Shanghai AI Lab / HKU 等 | 邊走邊看的線上時空理解 benchmark，模擬機器人探索時的空間記憶 | NeurIPS 2025 | 35 | [83](https://github.com/OpenRobotLab/OST-Bench) |

### 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-10 | [ClusterSplat](https://arxiv.org/abs/2610.36462) · [專案頁](https://jaesung8.github.io/clustersplat/) | KAIST | 在 3DGS 中做 3D grounding，不用閾值或 top-ratio 過濾，改以語意叢集選出目標 Gaussian，同時輸出 2D 遮罩與 3D Gaussian 集合 | ScanRefer 3D mIoU 23.33、mAcc@0.25 43.38（作者稱優於 LangSplat、OpenGaussian） | 未公開 | NeurIPS 2026 |
| 2026-10 | [P³-VLM](https://arxiv.org/abs/2610.28018) · [專案頁](https://p3vlm.insait.ai/) | INSAIT, Sofia Univ. | 指出 3D VLM 依賴 bounding box 造成語意洩漏，改用單一 3D 點當 prompt，三路徑（位置、任務、情境）架構、不需偵測器 | 點提示下 location-grounded captioning 52.1%（作者稱 SOTA）；盲 LLM 在 Nr3D 從 36.4% 降到 18.0% | 未公開 | NeurIPS 2026 |
| 2026-09 | [Stream3D-VLM](https://arxiv.org/abs/2606.06891) · [專案頁](https://stream3d-vlm.github.io/) | Zhejiang / Tencent Hunyuan / HKUST | 串流影像的線上 3D VLM：用自迴歸方式學何時該回答，並逐步注入對齊時間的幾何先驗 | 資料集超過 100 萬組 QA、29 種任務 | [GitHub](https://github.com/hanxunyu/Stream3D-VLM) | ECCV 2026 |
| 2026-09 | [OpenGround](https://arxiv.org/abs/2512.23020) · [專案頁](https://why-102.github.io/openground.io/) | Nanjing / China Mobile | 不靠預先定義的物件查找表，以任務鏈規劃並線上感知目標，處理未定義目標與複雜查詢 | OpenTarget 提升 17.6% | [GitHub](https://github.com/why-102/openground) | ECCV 2026 |

## 電腦視覺（偵測、分割、視覺基礎模型）

### 在解決的問題

- 開放詞彙：偵測、分割不限類別（CLIP、Grounding DINO、SAM 3）。
- 通用視覺特徵：自監督預訓練（DINO）供深度、匹配、分割等下游任務。
- 即時性：能在機上跑（RT-DETR、YOLO-World）。
- 時序一致：點追蹤、影片分割（CoTracker、SAM 2）。

### 重要論文（資料日期 2026-11-01）

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 奠基 | 引用、Star、HF | 2021 | [CLIP](https://arxiv.org/abs/2103.00020) | OpenAI | 影像-文字對比預訓練，開放詞彙感知的起點 | ICML 2021 | 59,251 | [34,553](https://github.com/openai/CLIP) |
| 奠基 | 引用、Star、獲獎 | 2023 | [SAM](https://arxiv.org/abs/2304.02643) · [專案頁](https://segment-anything.com) | Meta | 可提示的通用分割基礎模型 | ICCV 2023 | 16,651 | [55,084](https://github.com/facebookresearch/segment-anything) |
| 奠基 | 引用、獲獎 | 2021 | [Swin Transformer](https://arxiv.org/abs/2103.14030) | Microsoft Research Asia | 移位視窗的階層式 ViT，計算量隨解析度線性成長，可當偵測、分割通用骨幹 | ICCV 2021 | 37,367 | 未公開 |
| 奠基 | 引用、Star | 2023 | [DINOv2](https://arxiv.org/abs/2304.07193) | Meta | 自監督視覺特徵，免微調可用於深度、分割、匹配 | TMLR 2024 | 11,793 | [13,493](https://github.com/facebookresearch/dinov2) |
| 奠基 | 引用、Star | 2024 | [YOLOv10](https://arxiv.org/abs/2405.14458) | Tsinghua | 一致雙重標籤分配，免 NMS 的端到端 YOLO | NeurIPS 2024 | 6,477 | [11,338](https://github.com/THU-MIG/yolov10) |
| 奠基 | 引用、Star、HF | 2024 | [SAM 2](https://arxiv.org/abs/2408.00714) · [專案頁](https://ai.meta.com/sam2) | Meta | 支援影片的可提示分割 | ICLR 2025 | 4,745 | [20,084](https://github.com/facebookresearch/sam2) |
| 奠基 | 引用、Star、HF | 2025 | [DINOv3](https://arxiv.org/abs/2508.10104) · [專案頁](https://ai.meta.com/dinov3/) | Meta | 擴大規模並改善稠密特徵的自監督視覺模型 | arXiv | 1,883 | [11,660](https://github.com/facebookresearch/dinov3) |
| 奠基 | 引用、Star、HF | 2025 | [SAM 3](https://arxiv.org/abs/2511.16719) · [專案頁](https://ai.meta.com/sam3/) | Meta | 以概念（文字／範例）提示的分割與追蹤 | arXiv | 1,386 | [12,166](https://github.com/facebookresearch/sam3) |
| 奠基 | 引用、Star | 2022 | [YOLOv7](https://arxiv.org/abs/2207.02696) | Academia Sinica | E-ELAN 架構加重參數化訓練技巧的即時偵測器 | CVPR 2023 | 11,602 | [14,158](https://github.com/WongKinYiu/yolov7) |
| 奠基 | 引用、Star | 2021 | [MAE](https://arxiv.org/abs/2111.06377) | Meta | 遮罩自編碼自監督預訓練 | CVPR 2022 | 13,491 | [8,360](https://github.com/facebookresearch/mae) |
| 奠基 | 引用、Star | 2023 | [Grounding DINO](https://arxiv.org/abs/2303.05499) | IDEA | 語言引導的開放集合物件偵測 | ECCV 2024 | 5,417 | [10,723](https://github.com/IDEA-Research/GroundingDINO) |
| 奠基 | 引用、Star | 2024 | [Grounded SAM](https://arxiv.org/abs/2401.14159) | IDEA | Grounding DINO + SAM 組合做開放詞彙分割 | arXiv | 1,407 | [17,791](https://github.com/IDEA-Research/Grounded-Segment-Anything) |
| 奠基 | 引用、Star | 2023 | [RT-DETR](https://arxiv.org/abs/2304.08069) · [專案頁](https://zhao-yian.github.io/RTDETR) | Baidu | 即時 DETR 偵測器 | CVPR 2024 | 4,923 | [5,640](https://github.com/lyuwenyu/RT-DETR) |
| 奠基 | 引用、Star | 2023 | [SigLIP](https://arxiv.org/abs/2303.15343) | Google | sigmoid 損失的影像-文字預訓練，多數 VLM 的視覺編碼器 | ICCV 2023 | 4,217 | [3,566](https://github.com/google-research/big_vision) |
| 奠基 | 引用、Star、HF | 2024 | [YOLO-World](https://arxiv.org/abs/2401.17270) | Tencent | 即時開放詞彙偵測 | CVPR 2024 | 1,173 | [6,594](https://github.com/AILab-CVC/YOLO-World) |
| 奠基 | 引用、Star、HF | 2023 | [FastSAM](https://arxiv.org/abs/2306.12156) | CAS / UCAS | 以 YOLOv8-seg 實例分割取代 SAM，大幅加速 | arXiv | 606 | [8,428](https://github.com/CASIA-IVA-Lab/FastSAM) |
| 奠基 | 引用、Star | 2023 | [LightGlue](https://arxiv.org/abs/2306.13643) | ETH | 快速自適應的特徵匹配，SLAM 前端常用 | ICCV 2023 | 1,321 | [4,855](https://github.com/cvg/LightGlue) |
| 奠基 | 引用、Star、HF | 2025 | [Perception Encoder](https://arxiv.org/abs/2504.13181) | Meta | 對比式圖文預訓練，對齊中間層特徵供各下游任務 | NeurIPS 2025 | 404 | [2,404](https://github.com/facebookresearch/perception_models) |
| 奠基 | 引用、Star | 2023 | [MobileSAM](https://arxiv.org/abs/2306.14289) | Kyung Hee | 解耦蒸餾 SAM 影像編碼器，行動裝置可跑 | arXiv | 731 | [5,905](https://github.com/ChaoningZhang/MobileSAM) |
| 奠基 | 引用、Star | 2023 | [SEEM](https://arxiv.org/abs/2304.06718) | UW-Madison / Microsoft / HKUST | 點框文字音訊等多種提示統一的互動分割 | NeurIPS 2023 | 920 | [4,788](https://github.com/UX-Decoder/Segment-Everything-Everywhere-All-At-Once) |
| 奠基 | 引用、Star | 2023 | [CoTracker](https://arxiv.org/abs/2307.07635) · [專案頁](https://co-tracker.github.io/) | Meta / Oxford | 聯合追蹤大量點的影片點追蹤 | ECCV 2024 | 710 | [5,183](https://github.com/facebookresearch/co-tracker) |
| 奠基 | 引用、Star | 2023 | [HQ-SAM](https://arxiv.org/abs/2306.01567) | HKUST / ETH / Dartmouth | 加入高品質輸出 token 提升 SAM 遮罩邊緣 | NeurIPS 2023 | 728 | [4,265](https://github.com/SysCV/sam-hq) |
| 奠基 | 引用、Star | 2021 | [LoFTR](https://arxiv.org/abs/2104.00680) · [專案頁](https://zju3dv.github.io/loftr/) | Zhejiang / SenseTime | 無偵測器的 Transformer 粗到細半稠密匹配 | CVPR 2021 | 2,195 | [2,977](https://github.com/zju3dv/LoFTR) |
| 奠基 | 引用、Star | 2024 | [DEIM](https://arxiv.org/abs/2412.04234) · [專案頁](https://www.shihuahuang.cn/DEIM/) | Intellindust / CityU / Great Bay | 稠密一對一匹配加速 DETR 收斂 | CVPR 2025 | 435 | [1,646](https://github.com/ShihuaHuang95/DEIM) |
| 奠基 | 引用、Star、HF、獲獎 | 2024 | [Molmo](https://arxiv.org/abs/2409.17146) | AI2 / University of Washington | 不蒸餾私有 VLM，全靠人工收集的 PixMo 資料訓練開放 VLM，並能以點指出物件位置 | CVPR 2025 | 344 | [943](https://github.com/allenai/molmo) |
| 奠基 | 引用 | 2021 | [ViLD](https://arxiv.org/abs/2104.13921) | Google / NVIDIA | 把 CLIP 知識蒸餾到偵測器做開放詞彙偵測 | ICLR 2022 | 1,459 | 未公開 |
| 奠基 | 引用、HF | 2023 | [Florence-2](https://arxiv.org/abs/2311.06242) | Microsoft | 統一提示式文字輸出的多任務視覺基礎模型 | CVPR 2024 | 690 | 未公開 |
| 主流 | 引用、Star、知名 | 2023 | [Track Anything](https://arxiv.org/abs/2304.11968) | SUSTech | SAM 結合 XMem 的互動式影片物件追蹤 | arXiv | 365 | [7,014](https://github.com/gaomingqi/Track-Anything) |
| 主流 | 引用、Star、知名 | 2024 | [SAMURAI](https://arxiv.org/abs/2411.11922) · [專案頁](https://yangchris11.github.io/samurai/) | UW | SAM 2 加運動感知記憶選擇的零樣本追蹤 | arXiv | 157 | [7,120](https://github.com/yangchris11/samurai) |
| 主流 | Star、HF | 2026 | [V-JEPA 2.1](https://arxiv.org/abs/2603.14482) | Meta FAIR / Zaragoza | 改善影片自監督學習的稠密特徵，同時提升世界模型、導航與深度估計；TartanDrive ATE 5.687 | ECCV 2026 | 157 | [4,839](https://github.com/facebookresearch/vjepa2) |
| 主流 | 引用、Star、知名 | 2024 | [CoTracker3](https://arxiv.org/abs/2410.11831) · [專案頁](https://cotracker3.github.io/) | Meta / Oxford | 以偽標籤在真實影片半監督訓練的簡化點追蹤 | arXiv | 197 | [5,183](https://github.com/facebookresearch/co-tracker) |
| 主流 | 引用、Star、知名 | 2023 | [OWLv2](https://arxiv.org/abs/2306.09683) | Google DeepMind | 網路圖文對自訓練偽標註，擴大開放詞彙偵測 | NeurIPS 2023 | 519 | [3,847](https://github.com/google-research/scenic) |
| 主流 | 引用、Star、知名 | 2022 | [OWL-ViT](https://arxiv.org/abs/2205.06230) | Google | 用 CLIP 式骨幹做開放詞彙偵測 | ECCV 2022 | 471 | [3,847](https://github.com/google-research/scenic) |
| 主流 | Star、HF、推薦 | 2026 | [YOLO26](https://arxiv.org/abs/2606.03748) · [專案頁](https://docs.ultralytics.com/models/yolo26/) | Ultralytics | 雙頭架構原生免 NMS、移除 DFL，並用混合優化器與小物件標籤分配同時涵蓋偵測、分割、姿態等任務；COCO mAP 40.9–57.5，T4 TensorRT 1.7–11.8 ms；程式碼為 AGPL-3.0 | arXiv | 201 | [63,016](https://github.com/ultralytics/ultralytics) |
| 主流 | 引用、Star、知名 | 2023 | [EfficientSAM](https://arxiv.org/abs/2312.00863) · [專案頁](https://yformer.github.io/efficient-sam/) | Meta | 以 SAM 特徵遮罩重建預訓練輕量分割模型 | CVPR 2024 | 334 | [2,499](https://github.com/yformer/EfficientSAM) |
| 主流 | Star、HF、獲獎 | 2026 | [Molmo2](https://arxiv.org/abs/2601.10611) | AI2 | 把 Molmo 延伸到影片理解與時空 grounding，資料與權重全開放 | CVPR 2026 | 170 | [753](https://github.com/allenai/molmo2) |
| 主流 | 引用、Star、知名 | 2024 | [XFeat](https://arxiv.org/abs/2404.19174) | UFMG / Google / Univ. Bourgogne 等 | CPU 也能即時的輕量特徵偵測與匹配 | CVPR 2024 | 275 | [1,758](https://github.com/verlab/accelerated_features) |
| 主流 | 引用、Star、獲獎、知名 | 2023 | [OmniMotion](https://arxiv.org/abs/2306.05422) · [專案頁](https://omnimotion.github.io/) | Cornell / Google / UC Berkeley | 測試時最佳化全域一致的準 3D 表示，對整段影片每個像素做長時距、跨遮擋追蹤 | ICCV 2023 | 256 | [2,269](https://github.com/qianqianwang68/omnimotion) |
| 主流 | 引用、Star、知名 | 2023 | [RoMa](https://arxiv.org/abs/2305.15404) · [專案頁](https://parskatt.github.io/RoMa/) | Linköping / ECUST / Chalmers | DINOv2 粗特徵加分類式回歸的穩健稠密匹配 | CVPR 2024 | 479 | [1,326](https://github.com/Parskatt/RoMa) |
| 主流 | 引用、Star、知名 | 2024 | [Efficient LoFTR](https://arxiv.org/abs/2403.04765) · [專案頁](https://zju3dv.github.io/efficientloftr/) | Zhejiang | 聚合注意力讓半稠密匹配接近稀疏方法速度 | CVPR 2024 | 290 | [1,063](https://github.com/zju3dv/EfficientLoFTR) |
| 主流 | 引用、Star、基準 | 2022 | [TAP-Vid](https://arxiv.org/abs/2211.03726) · [專案頁](https://tapvid.github.io/) | Google DeepMind / Oxford | 定義任意點追蹤任務並提供真實影片標註基準 | NeurIPS 2022 | 350 | [2,248](https://github.com/google-deepmind/tapnet) |
| 主流 | 引用、Star、知名 | 2021 | [RegionCLIP](https://arxiv.org/abs/2112.09106) | Microsoft / UW-Madison | 區域與文字對齊預訓練，用於開放詞彙偵測 | CVPR 2022 | 1,025 | [819](https://github.com/microsoft/RegionCLIP) |
| 主流 | 引用、Star、獲獎、知名 | 2024 | [SEA-RAFT](https://arxiv.org/abs/2405.14793) | Princeton | 改用混合 Laplace 損失、直接回歸初始光流並以剛體運動預訓練，比 RAFT 更快更準 | ECCV 2024 | 257 | [722](https://github.com/princeton-vl/SEA-RAFT) |
| 主流 | 引用、Star、獲獎、知名 | 2021 | [GMFlow](https://arxiv.org/abs/2111.13680) | Monash / Sydney / JD Explore | 以全域匹配取代 cost volume 迴歸的光流 | CVPR 2022 | 593 | [806](https://github.com/haofeixu/gmflow) |
| 新興 | 獲獎、推薦 | 2026 | [DeFM](https://arxiv.org/abs/2601.18923) · [專案頁](https://de-fm.github.io/) | ETH RSL / NVIDIA / UC Berkeley | DINO 式自蒸餾只在 6000 萬張深度圖上預訓練，加保留公制尺度的三通道正規化，再蒸餾成 3M 參數 CNN，凍結即可接導航、運動與操作策略 | T-RO 2026 | 11 | [274](https://github.com/leggedrobotics/defm) |
| 新興 | 獲獎、基準 | 2026 | [GuideTWSI](https://arxiv.org/abs/2603.07060) | UMass Amherst / UT Austin / Maine | 合成加真實的導盲磚分割資料集，用於視障者導航輔助 | ICRA 2026 | 2 | 未公開 |
| 新興 | 獲獎 | 2026 | [Day-to-Night Agri Translation](https://arxiv.org/abs/2607.12065) | Kennesaw State / Lincoln | 非監督式日轉夜跨模態影像轉換，用白天標註訓練夜間農業視覺導航 | IROS 2026 | 0 | 未公開 |

### 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
| --- | --- | --- | --- | --- | --- | --- |

## 模擬與 Real2Sim

### 在解決的問題

- 視覺擬真：模擬器畫面和真實影像有落差，改用 NeRF／3DGS 重建真實場景來渲染。
- 物理可用：重建的場景要有碰撞網格、關節、材質，才能互動與訓練。
- 低成本擷取：手機或手持相機掃描就能建。
- 在數位分身裡訓練或評估策略，再部署回實機（real-to-sim-to-real）。
- 另一路線是生成式 world model（如 Cosmos）直接產生訓練資料。

### 重要論文（資料日期 2026-11-01）

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 奠基 | 引用、Star、HF | 2025 | [Cosmos](https://arxiv.org/abs/2501.03575) · [專案頁](https://research.nvidia.com/labs/dir/cosmos1/) | NVIDIA | 物理 AI 的 world foundation model 平台 | arXiv | 996 | [12,221](https://github.com/NVIDIA/Cosmos) |
| 奠基 | 引用、Star、HF、機構 | 2025 | [V-JEPA 2](https://arxiv.org/abs/2506.09985) | Meta | 網路影片自監督預訓練，少量機器人資料即可規劃 | arXiv | 1,016 | [4,839](https://github.com/facebookresearch/vjepa2) |
| 奠基 | 引用、Star | 2023 | [Orbit / Isaac Lab](https://arxiv.org/abs/2301.04195) · [專案頁](https://isaac-orbit.github.io/) | NVIDIA / ETH | 基於 Isaac Sim 的機器人學習框架 | RA-L 2023 | 647 | [8,547](https://github.com/isaac-sim/IsaacLab) |
| 奠基 | 引用、Star、HF | 2025 | [GEN3C](https://arxiv.org/abs/2503.03751) · [專案頁](https://research.nvidia.com/labs/toronto-ai/GEN3C/) | NVIDIA / Toronto / Vector | 以 3D 快取引導影片生成，精準相機控制 | CVPR 2025 | 419 | [1,445](https://github.com/nv-tlabs/GEN3C) |
| 奠基 | 引用、Star | 2021 | [Isaac Gym](https://arxiv.org/abs/2108.10470) · [專案頁](https://sites.google.com/view/isaacgym-nvidia) | NVIDIA | GPU 端到端物理模擬，大規模平行 RL | NeurIPS 2021 | 2,072 | [2,950](https://github.com/isaac-sim/IsaacGymEnvs) |
| 奠基 | 引用、Star、基準 | 2024 | [ManiSkill3](https://arxiv.org/abs/2410.00425) · [專案頁](http://maniskill.ai/) | UCSD / Hillbot | GPU 平行模擬與渲染的通用操作平台 | arXiv | 381 | [3,478](https://github.com/haosulab/ManiSkill) |
| 奠基 | 引用、Star、基準、機構 | 2024 | [SIMPLER](https://arxiv.org/abs/2405.05941) · [專案頁](https://simpler-env.github.io/) | UCSD / Stanford / Google DeepMind 等 | 縮小視覺與控制差距，用模擬評估真實操作策略 | CoRL 2024 | 641 | [1,181](https://github.com/simpler-env/SimplerEnv) |
| 奠基 | 引用、Star、基準、機構 | 2025 | [MuJoCo Playground](https://arxiv.org/abs/2502.08844) · [專案頁](https://playground.mujoco.org/) | UC Berkeley / Google DeepMind / Toronto 等 | 基於 MJX 的 GPU 模擬，分鐘級訓練並零樣本轉移 | arXiv | 135 | [2,269](https://github.com/google-deepmind/mujoco_playground) |
| 奠基 | 引用 | 2025 | [PhysTwin](https://arxiv.org/abs/2503.17973) · [專案頁](https://jianghanxiao.github.io/phystwin-web/) | Columbia / UIUC | 從稀疏互動影片重建彈簧質點物理的變形物件分身 | ICCV 2025 | 139 | [481](https://github.com/Jianghanxiao/PhysTwin) |
| 奠基 | 推薦 |  | [World Labs Atlas](https://www.worldlabs.ai/blog/atlas) | World Labs | 文字／影像／影片／3D 通用模型，可從手機影片重建場景並生成模擬用 RGB-D | 部落格 2026 | 0 | 未公開 |
| 主流 | 引用、Star、基準 | 2023 | [Infinigen](https://arxiv.org/abs/2306.09310) · [專案頁](https://infinigen.org) | Princeton | 全程序化生成無限照片級自然場景 | CVPR 2023 | 221 | [7,372](https://github.com/princeton-vl/infinigen) |
| 主流 | 引用、Star | 2021 | [Habitat 2.0](https://arxiv.org/abs/2106.14405) · [專案頁](https://aihabitat.org/) | Meta | 可互動的室內重建場景模擬器，具身 AI 標準平台 | NeurIPS 2021 | 855 | [3,179](https://github.com/facebookresearch/habitat-lab) |
| 主流 | 引用、Star、基準 | 2023 | [Habitat 3.0](https://arxiv.org/abs/2310.13724) · [專案頁](http://aihabitat.org/habitat3) | Meta | 加入人形化身與真人在環的人機協作模擬平台 | ICLR 2024 | 354 | [3,179](https://github.com/facebookresearch/habitat-lab) |
| 主流 | 引用、Star、HF | 2025 | [Lyra](https://arxiv.org/abs/2509.19296) · [專案頁](https://research.nvidia.com/labs/toronto-ai/lyra/) | NVIDIA / Toronto / Vector 等 | 影片擴散模型自蒸餾成 3DGS 場景生成 | arXiv | 44 | [2,799](https://github.com/nv-tlabs/lyra) |
| 主流 | 引用、Star、基準、機構 | 2025 | [RoboVerse](https://arxiv.org/abs/2504.18904) · [專案頁](https://roboverseorg.github.io/) | UC Berkeley / PKU / USC 等 | 統一多種模擬器的機器人資料與基準平台 | arXiv | 83 | [1,878](https://github.com/RoboVerseOrg/RoboVerse) |
| 主流 | 引用、Star、HF | 2025 | [GigaWorld-0](https://arxiv.org/abs/2511.19861) · [專案頁](https://giga-world-0.github.io/) | GigaAI | 影片生成加 3D 生成的世界模型作為 VLA 資料引擎 | arXiv | 56 | [1,618](https://github.com/open-gigaai/giga-world-0) |
| 主流 | 引用、Star、機構 | 2025 | [RWM](https://arxiv.org/abs/2501.10100) · [專案頁](https://sites.google.com/view/roboticworldmodel) | ETH | 自迴歸神經模擬器，想像中訓練策略並實機部署 | arXiv | 75 | [697](https://github.com/leggedrobotics/robotic_world_model) |
| 主流 | 引用、Star、HF、基準 | 2024 | [GRUtopia](https://arxiv.org/abs/2407.10943) · [專案頁](https://internrobotics.github.io/user_guide/internutopia/) | Shanghai AI Lab / Zhejiang / SJTU 等 | 十萬互動場景的城市級具身模擬社會 | arXiv | 87 | [1,306](https://github.com/openrobotlab/grutopia) |
| 主流 | 引用 | 2024 | [RialTo](https://arxiv.org/abs/2403.03949) · [專案頁](https://real-to-sim-to-real.github.io/RialTo/) | MIT | 真實場景重建成模擬環境，在模擬中強化學習修正策略 | RSS 2024 | 251 | [223](https://github.com/real-to-sim-to-real/RialToPolicyLearning) |
| 主流 | Star | 2026 | [World Model for Robot Learning Survey](https://arxiv.org/abs/2605.00080) · [專案頁](https://ntumars.github.io/wm-robot-survey/) | NTU | 整理機器人學習用的世界模型典範、應用與挑戰，並持續維護論文清單 | arXiv | 54 | [873](https://github.com/NTUMARS/Awesome-World-Model-for-Robotics-Policy) |
| 主流 | 引用、基準 | 2021 | [HM3D](https://arxiv.org/abs/2109.08238) · [專案頁](https://aihabitat.org/datasets/hm3d/) | Meta / UT Austin / Georgia Tech 等 | 千棟真實建築 3D 重建的具身 AI 場景資料集 | NeurIPS 2021 | 886 | [216](https://github.com/facebookresearch/habitat-matterport3d-dataset) |
| 主流 | 引用、機構 | 2025 | [R2R2R](https://arxiv.org/abs/2505.09601) · [專案頁](https://real2render2real.com) | UC Berkeley / TRI | 手機掃描加人類示範影片渲染訓練資料，免動力學模擬 | CoRL 2025 | 76 | [377](https://github.com/uynitsuj/real2render2real) |
| 主流 | Star、推薦 | 2026 | [TripoSplat](https://arxiv.org/abs/2605.16355) | Tsinghua / VAST | 高斯中心由學到的密度取樣，利於生成式建模 | SIGGRAPH 2026 | 4 | [1,421](https://github.com/VAST-AI-Research/TripoSplat) |
| 主流 | 引用 | 2025 | [ArtGS](https://arxiv.org/abs/2502.19459) · [專案頁](https://articulate-gs.github.io) | Tsinghua / BIGAI / PKU | 規範高斯加骨架式變形建模多部件關節物件 | ICLR 2025 | 79 | [83](https://github.com/YuLiu-LY/ArtGS) |
| 主流 | 引用、基準 | 2025 | [TartanGround](https://arxiv.org/abs/2505.10696) · [專案頁](https://tartanair.org/tartanground) | ETH RSL / CMU 等 | 大規模模擬地面機器人感知與導航資料集 | IROS 2025 | 50 | [129](https://github.com/castacks/tartanairpy) |
| 主流 | 引用、推薦 | 2025 | [VR-Robo](https://arxiv.org/abs/2502.01536) · [專案頁](https://vr-robo.github.io/) | Tsinghua | 3DGS 重建場景做視覺導航與運動控制的 real-to-sim-to-real | RA-L 2025 | 40 | [196](https://github.com/zst1406217/VR-Robo) |
| 主流 | 引用、HF、基準 | 2025 | [InternScenes](https://arxiv.org/abs/2509.10813) · [專案頁](https://marjordcpz.github.io/InternScenes.github.io/) | Shanghai AI Lab / SJTU / Beihang 等 | 含真實佈局與小物件的大規模可模擬室內場景 | NeurIPS 2025 | 32 | [277](https://github.com/InternRobotics/InternScenes) |
| 主流 | 引用、推薦 | 2025 | [GaussGym](https://arxiv.org/abs/2510.15352) · [專案頁](https://escontrela.me/gauss_gym/) | UC Berkeley / ETH / Amazon FAR | 3DGS 嵌入 IsaacGym 向量化渲染，從像素學運動 | arXiv | 34 | 未公開 |
| 新興 | 推薦 | 2026 | [SimFoundry](https://arxiv.org/abs/2606.28276) · [專案頁](https://research.nvidia.com/labs/gear/simfoundry/) | NVIDIA / Stanford / Georgia Tech / UT Austin 等 | 單支真實場景影片自動拆成遮罩、深度、2D→3D 物件網格與 3DGS 背景並做物理檢查，各模組可隨基礎模型替換，另生成 digital cousins 擴增訓練 | NVIDIA Research、arXiv | 30 | [446](https://github.com/NVlabs/SimFoundry) |
| 新興 | 推薦 | 2026 | [GATOR](https://arxiv.org/abs/2610.11215) · [專案頁](https://research.nvidia.com/labs/lpr/gator/) | NVIDIA / Simon Fraser | 從雜亂場景的隨手拍照片生成完整物件與場景相對位姿，再由 agent 在 Blender 編輯網格、只保留與原圖相符的修改，免重訓生成器 | NVIDIA Research、arXiv | 0 | 未公開 |

### 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-10 | [GRASE](https://arxiv.org/abs/2610.21498) | 西安交通大學、福州大學、Adobe、西湖大學 | 把影片當持續參照的 agent 流程：渲染結果與影像不符就回頭修正房間結構與物件擺放，而非一次到底 |  | 未公開 | arXiv |
| 2026-09 | [SPEAR](https://arxiv.org/abs/2607.06701) · [專案頁](https://mikeroberts3000.github.io/papers/spear) | Adobe / Intel Labs / Manycore / NVIDIA | Python 函式庫，可程式化控制任何 Unreal Engine 應用，並提供其他 UE 模擬器沒有的真值影像 | 開放超過 1.4 萬個 UE 函式 | [GitHub](https://github.com/spear-sim/spear) | ECCV 2026 |
| 2026-09 | [Habitat-GS](https://arxiv.org/abs/2604.12626) · [專案頁](https://zju3dv.github.io/habitat-gs/) | Zhejiang | 擴充 Habitat-Sim，以 3DGS 渲染場景並加入可驅動的高斯人體，用於訓練人感知導航 |  | [GitHub](https://github.com/zju3dv/habitat-gs) | ECCV 2026 |
| 2026-09 | [ReVeal](https://arxiv.org/abs/2609.23910) | Purdue / Samsung SDS | 考慮重建品質的 real-to-sim VLA 策略評估 |  | 未公開 | arXiv |

更早的 5 篇見 [topics/real2sim.md](topics/real2sim.md)。

## 月報

- [2026-11](digests/2026-11.md)
- [2026-10](digests/2026-10.md)
