# 3D 場景重建（feed-forward、SfM、3DGS／NeRF）

## 在解決的問題

- feed-forward 重建：不跑 SfM 優化，一次前向得到相機與幾何；挑戰在大規模與串流輸入。
- 傳統 SfM 的速度與穩健度：全域最佳化、位姿圖初始化。
- 3D 表示：3DGS 取代 NeRF，可即時渲染；表面品質與無位姿輸入仍在改進。
- 動態場景：同時重建幾何、運動與相機。

## 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-11 | [Anchor3R](https://arxiv.org/abs/2606.05035) | UCAS / Horizon Robotics / HKUST | 以當前幀為座標中心預測視窗相對位姿與局部幾何，重疊預測組成相對位姿圖，做線上更新與含回環的運動平均 | 只用 48 幀訓練，可處理超過 10,000 幀串流且 GPU 記憶體有界 | [GitHub](https://github.com/polar-explorer/Anchor3R) | CoRL 2026 |
| 2026-10 | [ACE-Zero + PGO](https://arxiv.org/abs/2610.35501) · [專案頁](https://eldentse.github.io/visual_localization_pgo_public/) | dConstruct Robotics / NUS | 在 ACE-Zero 上加 pose graph optimization，由預測的 scene coordinate 取相對位姿，並以對極與光流一致性估信心來抑制錯誤修正 |  | 未公開 | CVPR 2026 |
| 2026-09 | [FILT3R](https://arxiv.org/abs/2603.18493) | KAIST | 串流重建的狀態更新改用 token 空間的 Kalman 式增益，免訓練即可外掛，改善長序列穩定度 |  | [GitHub](https://github.com/jinotter3/FILT3R) | ECCV 2026 |
| 2026-09 | [OVGGT](https://arxiv.org/abs/2603.05959) · [專案頁](https://vaisr.github.io/OVGGT/) | NTU / NTUST | 壓縮 KV cache 並保護座標關鍵 token，免訓練把串流 VGGT 的記憶體與計算量壓到固定額度 |  | [GitHub](https://github.com/VAISR/OVGGT) | ECCV 2026 |
| 2026-04 | [Feed-forward 3D scene modeling survey](https://arxiv.org/abs/2604.14025) · [專案頁](https://ff3d-survey.github.io) | Zhejiang / NTU / Monash / ETH / Tübingen | feed-forward 3D 重建綜述，涵蓋 Point3R、IncVGGT、ZipMap 等串流／增量版本 |  | [GitHub](https://github.com/ziplab/Awesome-Feed-Forward-3D) | arXiv |
| 2026-02 | [LongStream](https://arxiv.org/abs/2602.13172) · [專案頁](https://3dagentworld.github.io/longstream/) | Horizon Robotics / CSU / ZJU | 快取一致訓練加定期刷新，抑制超長序列的注意力偏差，達到公里級公制尺度串流重建 | 18 FPS | [GitHub](https://github.com/3DAgentWorld/LongStream) | CVPR 2026 |
| 2026-02 | [VGG-T³](https://arxiv.org/abs/2602.23361) · [專案頁](https://research.nvidia.com/labs/dvl/projects/vgg-ttt) | NVIDIA / Toronto | 大規模離線 feed-forward 重建 |  | [GitHub](https://github.com/nv-dvl/vgg-ttt) | CVPR 2026 |
| 2026-01 | [V-DPM](https://arxiv.org/abs/2601.09499) | Oxford VGG | 把 VGGT 延伸到動態點雲圖，同時恢復動態深度與每個點的 3D 運動 |  | [GitHub](https://github.com/eldar/vdpm) | arXiv |
| 2025-11 | [AMB3R](https://arxiv.org/abs/2511.20343) · [專案頁](https://hengyiwang.github.io/projects/amber) | UCL | feed-forward 公制尺度重建 + 稀疏體素後端，不微調即可延伸到 VO／SLAM |  | [GitHub](https://github.com/HengyiWang/amb3r) | CVPR 2026 |
