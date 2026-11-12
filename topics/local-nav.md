# 局部導航與規劃（diffusion / world model / 探索）

## 在解決的問題

- 從感測器直接輸出可行軌跡，取代手調的代價地圖與規劃器參數。
- 泛化到沒見過的環境與機體：靠跨機體資料或大規模模擬訓練。
- 多解行為（岔路要選一邊）用 diffusion 表達；預測動作後果再規劃則走向 world model。
- 安全保證：學習式策略沒有碰撞保證，常另外疊安全濾波器。

## 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-11 | [MessyNav](https://arxiv.org/abs/2611.07417) · [專案頁](https://messynav.github.io) | UC Berkeley / Stanford | VLM 先做 affordance 推理決定推開、拿起或避開擋路物件，再做任務規劃，零樣本互動式導航 | 移動操作機實機成功率比最強基線高 27 pp | 未公開 | CoRL 2026 |
| 2026-11 | [WAM-Nav](https://arxiv.org/abs/2606.04907) | CASIA / Nanjing Univ. / NUDT | 共享 DiT 做非對稱聯合擴散，同時生成長時域動作與短時域潛在視覺預想，單一策略支援影像目標、點目標與無目標探索 | ClutterScenes、InternScenes 影像目標 SR +15.7%、點目標 +3.3%；實機平均成功率 85% | [GitHub](https://github.com/CoRL-2026-WAM-Nav/WAM-Nav) | CoRL 2026 |
| 2026-11 | [G2-Nav](https://arxiv.org/abs/2607.16956) | NTU / VinUniversity | VLM 不直接規劃，而是把社交情境寫進 vision-language costmap，另驗證上游追蹤並加高頻安全檢查 | 非結構化環境實機社交導航 | [GitHub](https://github.com/centiLinda/G2-Nav) | CoRL 2026 |
| 2026-10 | [GLST](https://arxiv.org/abs/2610.17927) | Stanford / UC Berkeley / NVIDIA | 目標在執行中被改寫或新增的鏈式目標導航：潛在信念拆成全域／局部空間與長／短時間記憶，goal-conditioned reward 平衡探索與回訪 | 多地形模擬優於基線；Spot 實機驗證 | 未公開 | CoRL 2026 |
| 2026-10 | [SpatialBEV](https://arxiv.org/abs/2610.22900) · [專案頁](https://theairlab.org/spatial-bev-dynamics) | CMU AirLab / Penn State | 越野動力學模型每步在預測狀態周圍查詢 BEV 幾何與語意特徵當條件，不再只用整體環境特徵 | 跨季節資料預測誤差降 17.1%；≥10 m/s 實機最大橫向誤差降 25.3% | [GitHub](https://github.com/castacks/spatial-bev-dynamics) | CoRL 2026 |
| 2026-10 | [PathLift](https://arxiv.org/abs/2610.16103) · [專案頁](https://hyeongaa.github.io/pathlift) | Seoul National Univ. | 逐 waypoint 的深度條件 adapter，用感測器深度把通用視覺導航策略的無單位軌跡轉成度量路徑，不需測試時優化 | 多種導航策略在模擬與輪式實機（雙目、LiDAR 深度）閉環成功率皆提升 | 未公開 | CoRL 2026 |
| 2026-10 | [TravSUITE](https://arxiv.org/abs/2610.32130) | CMU / Field AI | 越野高速導航的可通行性系統：高效 voxel mapper 加自監督、含不確定性的 IRL，部署時依風險調整 | 實機導航錯誤減少 80%、穿越速度快 5% | 未公開 | RSS 2026 |
| 2026-10 | [RangeNav](https://arxiv.org/abs/2610.29845) · [專案頁](https://rangenav.github.io/) | ETH RSL / NVIDIA | 只用合成資料預訓練 183k 參數的 LiDAR range-image encoder（重建 + 語意分割 + BEV 預測），凍結後給 RL 導航策略 | 模擬 SR 比僅重建基線平均高 32.03 / 23.73 pp（訓練／OOD 環境）；Unitree B2-W 零樣本實機過人群與工地 | 未公開 | arXiv |
| 2026-10 | [Physical AI for Intralogistics](https://arxiv.org/abs/2610.28432) | Idealworks / NVIDIA | 把 NVIDIA X-Mobility 與 COMPASS 導航策略放進倉儲數位孿生訓練，再用 Cosmos 生成 sim-to-real 變體資料微調，部署在 Jetson AGX Xavier 差速底盤 | 實機四個場景成功率 65.3%（純模擬訓練）→ 91.7%（加 Cosmos 資料），與量產導航堆疊差 8.3 點 | 未公開 | arXiv |
| 2026-10 | [LiteNWM](https://arxiv.org/abs/2610.12368) | Nanjing Univ. / Imperial / Sony AI | 輕量潛空間 world model，可機上跑 | 實機未見場景 SR 43.3%（NoMaD）→ 83.3% | 未公開 | arXiv |
| 2026-09 | [ULVN](https://arxiv.org/abs/2608.06833) · [專案頁](https://hren20.github.io/ulvn-website) | Sun Yat-sen / Insta360 Research | 影像目標導航不需時序影片或深度：從無序影像建圖，用圖上信念傳播定位與規劃子目標；有實機部署 |  | [GitHub](https://github.com/hren20/ulvn) | ECCV 2026 |
| 2026-09 | [A scalar per patch](https://arxiv.org/abs/2606.21216) | NAVER LABS Europe | 大規模實機比較視覺編碼器，發現每個 patch 壓到單一純量仍足以支撐導航，且特徵可對應 affordance | 實體建築 966 個 episode、24 km | 未公開 | ECCV 2026 |
| 2026-09 | [RAE-NWM](https://arxiv.org/abs/2603.09241) | Tsinghua | 導航 world model 改在稠密 DINOv2 特徵空間做時序預測，不用壓縮後的 VAE latent，保留細部結構 |  | [GitHub](https://github.com/20robo/raenwm) | ECCV 2026 |
| 2026-09 | [UniWM](https://arxiv.org/abs/2510.08713) | University of Washington | 單一自迴歸骨幹同時做視覺預想與規劃，讓動作選擇直接依據想像結果，並加入記憶 | 導航成功率最高提升 30% | [GitHub](https://github.com/UWMILab/UniWM) | ECCV 2026 |
| 2026-07 | [X-NavDP](https://arxiv.org/abs/2607.28560) · [專案頁](https://yty-sky.github.io/x-navdp-project-page) | Shanghai AI Lab / Fudan / SYSU | NavDP 泛化到新行為與新機體（group Q-score reweighted matching） |  | 未公開 | CoRL 2026 |
