# 深度估計與 occupancy

## 在解決的問題

- 單眼公制深度：要有絕對尺度，且相機內參常未知。
- 雙目深度的零樣本泛化。
- 透明、反光表面讓深度感測器失效。
- occupancy：多源自自駕，室內與開放詞彙版本正在補上。

## 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-11 | [OptiGeo](https://arxiv.org/abs/2608.29881) · [專案頁](https://mx-liu6.github.io/OptiGeo-web/) | DiDi / HKU / SUSTech | 把透明、反光區的失敗歸因於真實深度監督的感測器偏差，用乾淨幾何教師與殘差修剪對齊修正，少量透明物渲染資料當乾淨監督 | 30M 參數在透明場景 benchmark 勝過 300M 單目與十億級多視角模型；一般零樣本深度仍具競爭力 | [GitHub](https://github.com/mx-liu6/OptiGeo) | CoRL 2026 |
| 2026-09 | [ZipDepth](https://arxiv.org/abs/2607.08771) · [專案頁](https://zipdepth.github.io/) | University of Bologna | 可重參數化編解碼器加多領域基礎模型蒸餾，讓輕量單目深度也有 zero-shot 泛化，可上嵌入式裝置 | 6.1M 參數 | [GitHub](https://github.com/fabiotosi92/ZipDepth) | ECCV 2026 |
| 2026-09 | [WAFT-Stereo](https://arxiv.org/abs/2603.24836) | Princeton | 證明雙目匹配不一定要 cost volume，只用 warping 就能達到領先表現 | ETH3D zero-shot 誤差降 81%；比競品快 1.8–6.7 倍 | [GitHub](https://github.com/princeton-vl/WAFT-Stereo) | ECCV 2026 |
| 2026-09 | [MetricAnything](https://arxiv.org/abs/2601.22054) · [專案頁](https://metric-anything.github.io/metric-anything-io/) | Li Auto | 隨機遮罩深度圖形成稀疏度量提示，讓模型能從雜訊大、來源不一的 3D 資料學度量深度 |  | [GitHub](https://github.com/metric-anything/metric-anything) | ECCV 2026 |
| 2026-09 | [MobileOcc](https://arxiv.org/abs/2511.16949) · [專案頁](https://autonomousrobots.nl/paper_websites/mobileocc) | TU Delft | 行人密集環境下給移動機器人用的語意 occupancy 資料集，用 mesh 優化標註可變形的人體佔據 |  | 未公開 | ECCV 2026 |
| 2026-09 | [Monocular Depth Estimation: Progress and Opportunities](https://arxiv.org/abs/2609.01172) | HKU | 單眼深度綜述 |  | [GitHub](https://github.com/CVMI-Lab/Depth_Survey) | arXiv |
| 2026-07 | [ARDepth](https://arxiv.org/abs/2607.12433) | SYSU / Baidu | 自回歸單眼深度估計 |  | 未公開 | arXiv |
