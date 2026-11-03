# Robot Perception Survey

- 加論文、擴充重要論文、新增主題時，先用 Skill 工具呼叫 `update-survey`（`.claude/skills/update-survey/`）。
- 實驗室清單在 `docs/labs.md`，直接改這個檔案。
- README 與 `docs/legged.md`、`docs/archive.md` 由 `scripts/build_readme.py` 產生，改 `topics/`、`data/`、`digests/` 後重跑，不手改。
- 一律用繁體中文（台灣用語）；commit message 用英文、conventional 前綴（`docs: ...`）。
- 範圍：AMR（輪式）、四足、輪足的導航，機器人用得到的視覺、3D 感知、SLAM、Real2Sim，以及 AMR 加手臂（移動操作）的感知。純操作策略與控制、固定手臂模仿學習、純人形全身控制、純自駕不收，除非方法可直接用在上述機體。

## 主題邊界

一篇只放一個主題，以主要貢獻判斷：

- `vln.md`：用語言或高階目標下指令的導航，含導航基礎模型、VLA。
- `local-nav.md`：不靠語言或語意目標的導航：從感測器到軌跡或速度的策略（diffusion、world model、RL）、幾何探索與路徑規劃、社交導航。
- `mobile-manip.md`：從導航銜接到操作的感知：抓取位姿感知、腕部與機身相機融合與目標遞交、base placement 感知、導航與操作共用的場景表示。物件位姿估計仍放 det3d，純給導航查詢的場景圖仍放 semantic-map，深度仍放 perception-3d。
- `quadruped.md` / `wheel-legged.md`：該機體特有的運動控制與導航。
- `slam.md`：SLAM、VO、LIO、重定位、回環。
- `reconstruction.md`：feed-forward 3D 重建、SfM、3DGS／NeRF 表示與渲染；產出是幾何與外觀。以軌跡或 ATE 為主要評估的線上追蹤放 slam；產出要能拿來模擬、訓練或評估策略（碰撞、物理、可互動物件）的放 real2sim。
- `perception-3d.md`：單目與雙目深度估計、occupancy。
- `semantic-map.md`：給導航查詢用的語意地圖、場景圖。
- `det3d.md`：點雲骨幹、3D 物件偵測、3D 語意／實例分割（含開放詞彙）、物件位姿估計。純自駕的室外 LiDAR／BEV 偵測不收。
- `spatial.md`：3D grounding、空間推理 VLM、3D-LLM 與其 benchmark；輸入或輸出是語言的 3D 理解放這裡，不經語言的放 det3d。以單一場景的理解為主；要累積成給導航查詢的地圖才放 semantic-map。
- `vision.md`：2D 偵測、分割、追蹤、視覺基礎模型。
- `real2sim.md`：模擬器與具身場景資料集、當模擬器用的 world model，以及把真實場景重建成可模擬、可訓練或可評估策略的環境。拿來當規劃器的 world model 歸它服務的導航主題。
