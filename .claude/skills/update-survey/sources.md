# 新論文的搜尋來源

改動來源清單時，同步改 `scripts/build_readme.py` 裡 README 的「定期追蹤的來源」；實驗室只改 `docs/labs.md`。

0. **先查重點來源**（最優先）：arXiv API 無法依機構篩選，所以先逐一查下列來源的近期發表，再做第 1 步。
   - **NVIDIA**（每次都要查）：
     - https://research.nvidia.com/research-area/robotics 、 https://research.nvidia.com/research-area/computer-vision ：依年份列出論文，只顯示年份，月份看論文網址 slug。網站常比 arXiv 晚上架，所以兩邊都要查。
     - https://research.nvidia.com/publications ：全部論文，`?page=N` 翻頁，只能依會議篩選（例如 CoRL `?f%5B0%5D=publication_events%3A35`），不能依領域篩選。
     - 實驗室：Seattle Robotics Lab https://research.nvidia.com/labs/srl 、GEAR https://research.nvidia.com/labs/gear/ 。
     - 程式碼：https://github.com/NVlabs 。
     - 再用 WebSearch `NVIDIA <主題關鍵字> <年月>` 補查 Isaac、Cosmos、GR00T 等產品線的技術報告。
     - research.nvidia.com/labs/ 首頁會擋爬蟲（403），直接用上面的子頁。
   - **企業**：Google DeepMind、Meta FAIR、Physical Intelligence、Skild AI、Mistral、Alibaba（AMAP、DAMO）、ByteDance Seed、Tencent Robotics X、Huawei、Unitree、LimX、ANYbotics、Boston Dynamics；另 Waymo、Sony AI、Adobe、Samsung、Baidu、Microsoft、Apple的研究單位也算名單內（不必每次查）。
   - **實驗室**：主要名單與擴充追蹤名單見 [docs/labs.md](../../../docs/labs.md)。只有主要名單影響收錄條件；擴充追蹤只用來找論文，不必每次查。
   - 查法：看上列頁面近期發表，或 WebSearch `<機構> <主題關鍵字> <年月>`。
1. **arXiv 新投稿**：
   - 主要用 RSS：`https://rss.arxiv.org/rss/cs.RO`、`https://rss.arxiv.org/rss/cs.CV`，一次請求拿到當天全部新投稿，再用下表關鍵字比對標題與摘要。RSS 只有當天，距上次更新超過一天的日子用下一項補。
   - 補查漏掉的日期用 arXiv API：`https://export.arxiv.org/api/query`（只能用 https，http 在雲端連不上），`search_query` 加 `submittedDate:[上次更新日 TO 今天]`，`sortBy=submittedDate`，`max_results=100`。請求間隔 3 秒以上，429 就退避重試；被擋住時在 PR 註明哪幾天沒查到。
   - **HF Daily Papers**：`https://huggingface.co/api/daily_papers?date=YYYY-MM-DD` 逐日查，挑與範圍相關的；按讚數是收錄條件「HF」的依據。
   - WebFetch 失敗時改用 curl。

   | 主題 | 分類 | 關鍵字（abs 或 ti，OR 串接） |
   |---|---|---|
   | vln | cs.RO, cs.CV | "vision-language navigation", "object goal navigation", "embodied navigation", "navigation foundation model" |
   | local-nav | cs.RO | "visual navigation" AND (diffusion OR "world model" OR "reinforcement learning"), "end-to-end navigation" |
   | semantic-map | cs.RO, cs.CV | "scene graph", "open-vocabulary map", "semantic mapping" |
   | mobile-manip | cs.RO, cs.CV | "mobile manipulation", "mobile manipulator", "6-DoF grasp", "grasp detection" AND robot, "base placement" |
   | quadruped | cs.RO | (quadruped OR legged) AND (perceptive OR navigation OR terrain) |
   | wheel-legged | cs.RO | "wheel-legged", "wheeled-legged", "legged-wheeled" |
   | slam | cs.RO, cs.CV | SLAM, "visual odometry", "LiDAR-inertial", "place recognition", relocalization |
   | reconstruction | cs.CV, cs.RO | "feed-forward reconstruction", "3D reconstruction" AND (VGGT OR pointmap), "structure from motion", "Gaussian splatting" |
   | perception-3d | cs.CV, cs.RO | "depth estimation", "stereo matching", occupancy |
   | det3d | cs.CV, cs.RO | "3D object detection" AND (indoor OR open-vocabulary), "3D instance segmentation", "point cloud" AND (segmentation OR backbone) |
   | spatial | cs.CV, cs.RO | "3D visual grounding", "spatial reasoning" AND (VLM OR "vision-language"), "3D LLM" |
   | vision | cs.CV | "open-vocabulary detection", "open-vocabulary segmentation", "vision foundation model", "real-time object detection", YOLO |
   | real2sim | cs.RO, cs.CV | "real-to-sim", real2sim, "digital twin" AND robot, "Gaussian splatting" AND simulation |

2. **補充來源**（WebSearch）：Science Robotics、T-RO、IJRR、RA-L、T-ASE、JFR、TPAMI、IJCV 新刊；當期 RSS / CoRL / ICRA / IROS / CVPR / ICCV / ECCV / 3DV / SIGGRAPH / WACV / NeurIPS / ICLR / ICML 接收論文；EMNLP、ACL 只看 VLN 相關。
   **會議接收名單**：名單一公布就逐一比對，不只靠 arXiv 關鍵字。2026-11 抽樣 RSS、ECCV 2026，人工判定範圍內 146 篇只收到 10 篇，其中 6 篇 venue 還停在 arXiv。可用來源：`roboticsconference.org/<年>/program/papers/`、`www.roboticsproceedings.org/rss<屆>/index.html`、`eccv.ecva.net/virtual/<年>/papers.html`。接收論文常沒有寫進 arXiv Comments，也可能換標題（LingBot-Map 官方名單上沒有 LingBot），所以比對時要連 `metrics.json` 的標題一起看。arXiv 標題搜尋 47/135 查不到，要再用 Semantic Scholar `paper/search/match` 補。

3. **篩選**：只有 arXiv、還沒正式刊登的論文，只收第 0 步主要名單（NVIDIA、企業、實驗室；不含擴充追蹤名單）內的企業與實驗室（官方 repo star ≥ 500 或使用者推薦的除外）；已被會議或期刊接收的不限機構。每主題每次最多收 5 篇，NVIDIA 的不佔名額。名額優先給第 0 步主要名單內的機構，其次依：有實機實驗 > 開源程式或權重 > 標準 benchmark 上宣稱 SOTA。純 benchmark 微幅改進、只在遙測或醫療影像上驗證的不收。機構以 arXiv 摘要頁或論文首頁的作者單位為準，「機構」欄要填。

## 得獎名單（擴充重要論文時查）

查 CVPR、ICCV、ECCV、3DV、ICRA、IROS、CoRL、RSS 的最佳論文（含入圍、honorable mention、各類別獎），符合範圍的收進 `classics.csv` 並標 `獲獎`，`award` 寫明得獎或入圍與獎項名。2021–2026 已全面查過一次（2026-10），2026-11 逐篇補上 `award`；之後每年各會議公布後補當年度，只列入圍的會議（ICRA、IROS 2026）在得獎者公布後把「入圍」改成「得獎」。

| 會議 | 來源 | 坑 |
|---|---|---|
| CVPR | `cvpr.thecvf.com/Conferences/<年>/News/...`、候選 `cvpr.thecvf.com/virtual/<年>/events/AwardCandidates<年>` | 2022 finalists、2024 candidates 沒有官方清單；IEEE TCPAMI 獎項頁有年份與獎項標錯，別當來源；`virtual/<年>/awards_detail` 列的是 highlight，看不出獎項；cvpr2021.thecvf.com 連不上 |
| ICCV / ECCV | `iccv<年>.thecvf.com`、`eccv<年>.ecva.net/virtual/<年>/awards_detail` | ICCV 候選名單多半不公開，只能從 ICCV Daily（rsipvision.com）零星找到 |
| 3DV | `3dvconf.github.io/<年>/awards/` 與同目錄 `award_candidates.csv` | 2021、2024 官網沒有得獎頁，只能靠大學新聞；2023 停辦 |
| ICRA | `<年>.ieee-icra.org/program/awards/`；2021 只有 RAS 獎項手冊 PDF（`ieee-ras.org/images/2021_ICRA_Awards_Brochure_v3.pdf`）；2022、2023 用 Robohub 轉載 | 官網常只列入圍，得獎者要等會後；2021 手冊 PDF 文字是 `(cid:N)` 編碼，字元 = chr(N+29)，且兩欄排版，入圍名單的類別要對前後文；Robohub 轉載的 `(WINNER)` 標在得獎論文之後 |
| IROS | `<年>.ieee-iros.org/program/awards/`；2022 用 `iros2022.org/2022/10/30/award-winners/`；2023 用 AIhub 轉載 | curl 直接抓官網會 403，改用 WebFetch；2021 網域已失效、2024 官網與 PaperCept 都擋；2025 官網憑證錯誤，入圍名單在 PaperCept 議程 `IROS25_ContentListWeb_<1-3>.html` 的「Award Finalists N」場次，不分獎項；2026 官網只列入圍，得獎者只有二手報導 |
| CoRL / RSS | `<年>.corl.org/program/awards`、`roboticsconference.org/<年>/program/awards/` | CoRL 2021–2023 獎項頁已失效（2021 用 Robohub 轉載的官方推文）；CoRL 2025 起是 Google Sites，名單在跳脫兩次的內嵌 HTML 裡，要 `html.unescape` 兩次再解析；RSS 2023、2024 官網只列入圍 |

- 得獎與否以官網為準；只有二手報導（新聞、X、實驗室網站）的寫成入圍，不寫得獎。
- 純操作、純人形、純自駕、無人機、純渲染品質改進的不收，即使得獎。
