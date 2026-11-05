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
| 2026-11 | [PadLoc](https://arxiv.org/abs/2611.05172) | HTW Berlin | 免訓練的平面圖定位後端：用主要牆向產生少量位姿候選、以遮罩 NCC 比對自由空間，再用移動位姿高斯混合貝氏濾波，取代稠密 (x,y,θ) 網格，狀態大小不隨軌跡增長 | Bonn LiLocBench 比 UnLoc 的 SR@1m 高 23–32 pp（輪式里程計）；Hilti-Trimble 純相機魚眼 5 條序列中 3 條 online SR@2m 0.90–0.98 | [GitHub](https://github.com/mbookhahn/padloc) | WACV 2027 |
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
