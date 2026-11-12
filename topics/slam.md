# SLAM 與定位

## 在解決的問題

- 退化場景：長廊、隧道、空曠處 LiDAR 或視覺特徵不足。
- 多感測器緊耦合：LiDAR、IMU、相機融合。
- 學習式前端：用 DROID、MASt3R、VGGT 等取代手工特徵，處理無紋理、免校正相機。
- 稠密且寫實的地圖：NeRF／3DGS SLAM。
- 大尺度、長期：回環、地點辨識、多機器人、場景隨時間變化。

## 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-11 | [PROSE](https://arxiv.org/abs/2606.16569) | ETH Zurich / Oxford | 免訓練、純 RGB 的自我視角場景配準：兩段影片各建物件層級 3D 場景圖，提示同一個 VLM 跨掃描配對物件，再以幾何共識求剛體轉換 | Aria Digital Twin、Aria Everyday Activities 配準精度勝過幾何與學習式場景圖基線（作者自報） | 未公開 | CoRL 2026 |
| 2026-11 | [Leg Odometry Contact Representation](https://arxiv.org/abs/2606.05501) | Embry–Riddle Aeronautical Univ. | 只用關節編碼器與 IMU：自監督去噪自編碼器加潛空間 GMM 給出連續支撐信念，調整 ESKF 的零速量測協方差，不需力感測器或接觸標註 | 模擬與實機地形里程計誤差最低（作者自報）；偽標籤分類準確度高不代表里程計較準 | [GitHub](https://github.com/egirgin/leg-odometry-contact-representation) | CoRL 2026 |
| 2026-11 | [MosaicIMU](https://arxiv.org/abs/2606.09355) | Tsinghua | 以原型路由器組合各載具專家特徵的 MoE 預訓練，新領域只加輕量殘差專家，搭配歷史感知 EKF | 平均 ATE、RTE-10s 比學習式基線降 40%、34% | [GitHub](https://github.com/zoujy02/MosaicIMU) | CoRL 2026 |
| 2026-10 | [FreeLoc](https://arxiv.org/abs/2610.05011) · [專案頁](https://zju3dv.github.io/freeloc/) | Zhejiang Univ. | 不建離線資料庫：線上對平面圖射線查詢取得位姿錨點，以擴散精修成連續位姿，並構建似然接直方圖濾波做序列定位 | 單幀與序列平面圖定位 SOTA 且即時（作者自報）；室內實機 | 未公開 | CoRL 2026 |
| 2026-10 | [RoMo-GS](https://arxiv.org/abs/2610.24605) · [專案頁](https://romo-gs.github.io) | Seoul National Univ. / RAI Institute | 線上 3DGS 建圖：每個高斯在曝光區間解析積分模擬動態模糊（O(1)），Hessian 剪枝限制高斯數量，聯合優化位姿與速度 | 渲染品質追平離線去模糊 3DGS 且快 15–150 倍；高斯數比線上基線少約 20% | 未公開 | CoRL 2026 |
| 2026-10 | [Line-Augmented cuVSLAM](https://arxiv.org/abs/2610.20958) | Analog Devices、NVIDIA | 在 NVIDIA cuVSLAM 加線特徵（Plücker 參數化、點線殘差進 Gauss-Newton 位姿解與滑窗 BA），點特徵稀少時自動加重線的權重，針對倉庫等低紋理場景 | RGB-D：TUM Freiburg3 22 條序列 ATE 降 38.5%，Replica 8 條降 30.1% | 未公開 | arXiv |
| 2026-09 | [UniSim-SLAM](https://arxiv.org/abs/2608.01706) · [專案頁](https://vision3d-lab.github.io/unisim-slam/) | UNIST | 前端兩視角追蹤、後端多視角子地圖優化，以統一的 Sim(3) 約束接合不同視角組合的 feed-forward 預測 | 未校正設定下 TUM RGB-D 軌跡誤差降 38.5%、7-Scenes 降 45.9% | [GitHub](https://github.com/vision3d-lab/UniSim-SLAM) | ECCV 2026 |
| 2026-09 | [Register Any Point](https://arxiv.org/abs/2512.01850) | Bonn / Stanford / RWTH Aachen | 把點雲配準當條件生成：用流場把雜訊點直接送到配準後的場景，不做對應匹配與位姿圖 |  | [GitHub](https://github.com/PRBonn/RAP) | ECCV 2026 |
| 2026-09 | [Scal3R](https://arxiv.org/abs/2609.04201) · [專案頁](https://linjohnss.github.io/scal3r/) | NYCU / NVIDIA | 凍結 CUT3R、STream3R 骨幹，只加約 1% 參數的位姿 token 對多個過去關鍵幀並行查相對位姿，再以線上位姿圖與回環融合，長影片不再累積漂移 | KITTI 平均 ATE 比線上基線降 60% 以上；回環示範 ATE 49.8 m → 6.4 m | [GitHub](https://github.com/NVlabs/scal3r) | ECCV 2026 |
| 2026-09 | [FFVO](https://arxiv.org/abs/2609.13733) | Waymo / UW | feed-forward 位姿解碼器做長距離 VO |  | 未公開 | arXiv |
| 2026-08 | [SuperMap](https://arxiv.org/abs/2608.22896) · [專案頁](https://superodometry.com/supermap) | CMU | 高頻幾何 SLAM 結合非同步開放詞彙感知的 4D 地圖，處理物件身分漂移與語意過期；有實機展示 |  | [GitHub](https://github.com/superxslam/SuperMap) | RSS 2026 |
| 2026-05 | [Dr-BA](https://arxiv.org/abs/2605.07041) | University of Toronto | 直接用 2D 旋轉雷達強度影像做 BA，不先抽點雲，也能在既有地圖上做純雷達定位 | 超過 200 km 道路資料、5 條路線 | [GitHub](https://github.com/utiasASRL/dr_ba) | RSS 2026 |
| 2026-05 | [FF-VIO-Init](https://arxiv.org/abs/2605.17327) | MBZUAI / HKUST (GZ) / Zhejiang | 單目 VIO 初始化改用 feed-forward 3D 模型預測點雲，不依賴視覺特徵對應 | 初始化資料長度通常低於 1.2 s、成功率超過 90% | [GitHub](https://github.com/Yuantai-Z/FF-VIO-Init) | RSS 2026 |
| 2026-04 | [BIEVR-LIO](https://arxiv.org/abs/2604.14421) · [專案頁](https://patripfr.github.io/bievr-lio/) | ETH ASL / RSL | 幾何資訊貧乏場景，用 bump image 強化 voxel map，不需額外感測器 |  | [GitHub](https://github.com/ethz-asl/BIEVR-LIO) | RSS 2026 |
| 2026-02 | [GrandTour](https://arxiv.org/abs/2602.18164) · [專案頁](https://grand-tour.leggedrobotics.com) | ETH 等 | 足式機器人多模態感知與 SLAM 資料集，作者稱是目前最大的開放足式資料集 |  | [GitHub](https://github.com/leggedrobotics/grand_tour_dataset) | arXiv |
| 2026-01 | [VGGT-SLAM 2.0](https://arxiv.org/abs/2601.19887) | MIT SPARK | 新 factor graph 設計消除子地圖對齊的 15-DoF 漂移與平面退化；直接用 VGGT attention 層驗證回環，不需額外訓練 | TUM 位姿誤差比 VGGT-SLAM 低約 23%；Jetson Thor 地面機器人即時運行 | [GitHub](https://github.com/MIT-SPARK/VGGT-SLAM) | RSS 2026 |
