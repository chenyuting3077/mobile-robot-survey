#!/usr/bin/env python3
"""把 topics/*.md、data/classics.csv（+ metrics.json）與最新月報組成一頁到底的 README.md。

topics/ 與 data/ 是資料來源，README 由本腳本產生，不要手改。
"""
import csv
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from harvest import THRESHOLD  # noqa: E402
from check_data import SUBS, check  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
TOPICS = [
    "vln", "local-nav", "mobile-manip", "quadruped", "wheel-legged",
    "slam", "reconstruction", "perception-3d", "semantic-map", "det3d", "spatial", "vision", "real2sim",
]
PAGES = {"quadruped", "wheel-legged"}
STAR_BAR = 500  # 收錄條件「Star」
# 多個模型共用的套件 repo：star 不全屬於單篇論文，分級與排序時最多算到 STAR_BAR，表格仍顯示實際數字
SHARED_REPOS = {"ultralytics/ultralytics"}
HF_BAR = 20  # 收錄條件「HF」：約是 2026-10 候選中按讚數的前 15%

HEADER = """# Robot Perception Survey

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
"""
DOC_NOTE = "<!-- 本檔由 scripts/build_readme.py 產生，請改 topics/、data/ 後重跑 -->\n\n"


def recent_table(latest: str, name: str, updated: str, prefix: str = "") -> str:
    """只顯示最近 3 個月；「日期」多半是 arXiv 首次提交年月，晚被接收的論文可能一補進來就落在更早的主題檔。"""
    y, m = int(updated[:4]), int(updated[5:7]) - 2
    if m < 1:
        y, m = y - 1, m + 12
    cutoff = f"{y}-{m:02d}"
    lines, hidden = [], 0
    for line in latest.splitlines():
        date = re.match(r"\| (\d{4}-\d{2}) \|", line)
        if date and date[1] < cutoff:
            hidden += 1
        else:
            lines.append(line)
    text = "\n".join(lines).strip()
    if hidden:
        text += f"\n\n更早的 {hidden} 篇見 [topics/{name}.md]({prefix}topics/{name}.md)。"
    return text


def anchor(title: str) -> str:
    # GitHub 標題錨點：小寫、去標點、空白轉 -
    s = re.sub(r"[^\w\- ]", "", title.lower(), flags=re.UNICODE)
    return s.replace(" ", "-")


def reasons(year: int, cites: int, stars: int, upvotes: int, venue: str, tags: str) -> list[str]:
    out = []
    if year in THRESHOLD and cites >= THRESHOLD[year]:
        out.append("引用")
    if stars >= STAR_BAR:
        out.append("Star")
    if upvotes >= HF_BAR:
        out.append("HF")
    manual = [t for t in tags.split(";") if t]
    # 刊在這兩本期刊直接算「獲獎」；頂會最佳論文、oral 要人工標
    if venue.startswith(("Science Robotics", "T-RO")) and "獲獎" not in manual:
        out.append("獲獎")
    return out + manual


def tier(year: int, cites: int, stars: int) -> str:
    bar = THRESHOLD.get(year)
    if year < 2021 or stars >= 10000 or (bar and cites >= 4 * bar):
        return "奠基"
    if stars >= STAR_BAR or (bar and cites >= bar):
        return "主流"
    return "新興"


def score(year: int, cites: int, stars: int) -> float:
    # 門檻只定到 2021–2025，範圍外的年份用最接近的門檻，當年度與舊論文才排得進來
    bar = THRESHOLD[min(max(year, min(THRESHOLD)), max(THRESHOLD))]
    return cites / bar + stars / STAR_BAR


def paper_link(r) -> str:
    if r["url"]:
        href = r["url"]
    elif r["id"].startswith("DOI:"):
        href = f"https://doi.org/{r['id'][4:]}"
    else:
        href = f"https://arxiv.org/abs/{r['id']}"
    link = f"[{r['name']}]({href})"
    return link + (f" · [專案頁]({r['project']})" if r["project"] else "")


def paper_stats(r, metrics) -> tuple[int, int, int]:
    p = metrics["papers"].get(r["id"]) or {}
    year = p.get("year") or (int("20" + r["id"][:2]) if r["id"][:2].isdigit() else 0)
    return year, p.get("citationCount") or 0, metrics["stars"].get(r["repo"]) or 0


def ranked_stars(r, stars: int) -> int:
    return min(stars, STAR_BAR) if r["repo"] in SHARED_REPOS else stars


def classics_table(rows, metrics) -> str:
    items = []
    for r in rows:
        year, cites, stars = paper_stats(r, metrics)
        upvotes = metrics.get("hf", {}).get(r["id"]) or 0
        items.append((r, year, cites, stars, upvotes, tier(year, cites, ranked_stars(r, stars))))
    order = {"奠基": 0, "主流": 1, "新興": 2}
    items.sort(key=lambda x: (order[x[5]], -score(x[1], x[2], ranked_stars(x[0], x[3]))))

    lines = ["| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |",
             "|---|---|---|---|---|---|---|---|---|"]
    for r, year, cites, stars, upvotes, t in items:
        star = f"[{stars:,}](https://github.com/{r['repo']})" if r["repo"] else "未公開"
        why = "、".join(reasons(year, cites, stars, upvotes, r["venue"], r["tags"]))
        lines.append(f"| {t} | {why} | {year or ''} | {paper_link(r)} | {r['org']} | {r['note']} "
                     f"| {r['venue']} | {cites:,} | {star} |")
    return "\n".join(lines)


def main() -> None:
    if errors := check(TOPICS):
        sys.exit("資料格式錯誤，README 未產生：\n" + "\n".join(errors))
    classics = list(csv.DictReader((ROOT / "data" / "classics.csv").open()))
    metrics = json.loads((ROOT / "data" / "metrics.json").read_text())

    digests = sorted((ROOT / "digests").glob("*.md"), reverse=True)
    latest = digests[0].read_text()
    updated = re.search(r"最後更新：(\S+)", latest).group(1)

    sections = []
    for name in TOPICS:
        text = (ROOT / "topics" / f"{name}.md").read_text().strip()
        title, body = text.split("\n", 1)
        title = title.lstrip("# ").strip()
        problems, recent = body.split("## 最新論文", 1)
        problems = problems.replace("## 在解決的問題", "").strip()
        rows = [r for r in classics if r["topic"] == name]
        h = "##"
        parts = [f"{h} {title}", f"{h}# 在解決的問題", problems]
        if rows:
            parts.append(f"{h}# 重要論文（資料日期 {metrics['fetched']}）")
            for sub in SUBS.get(name, [""]):
                group = [r for r in rows if r["sub"] == sub]
                parts += ([f"{h}## {sub}"] if sub else []) + [classics_table(group, metrics)]
        parts += [f"{h}# 最新論文", recent_table(recent, name, updated, "../" if name in PAGES else "")]
        sections.append((title, name, "\n\n".join(parts)))

    legged = [(t, s) for t, n, s in sections if n in PAGES]
    toc = "\n".join(f"- [{t}](#{anchor(t)})" for t, _ in legged)
    (ROOT / "docs" / "legged.md").write_text(DOC_NOTE + "\n\n".join(["# 四足與輪足", toc] + [s for _, s in legged]) + "\n")

    archive = list(csv.DictReader((ROOT / "data" / "archive.csv").open()))
    parts = ["# 封存區", f"從重要論文移出但保留備查，規則見 [README](../README.md#怎樣算重要論文)，共 {len(archive)} 篇。"]
    for title, name, _ in sections:
        for reason in sorted({r["reason"] for r in archive if r["topic"] == name}):
            parts += [f"## {title}：{reason}",
                      classics_table([r for r in archive if r["topic"] == name and r["reason"] == reason], metrics)]
    (ROOT / "docs" / "archive.md").write_text(DOC_NOTE + "\n\n".join(parts) + "\n")

    trend = latest.split("## 趨勢", 1)[1].split("\n## ", 1)[0].strip()

    out = [HEADER, f"最後更新：{updated}\n", "## 目錄\n"]
    out.append(f"- [本月趨勢（{digests[0].stem}）](#本月趨勢{anchor(digests[0].stem)})")
    # 順序跟正文一致：先列 README 內的主題，獨立頁面放後面，否則點到中間會跳離本頁
    out += [f"- [{t}](#{anchor(t)})" for t, n, _ in sections if n not in PAGES]
    out.append("- [月報](#月報)")
    out.append("- [四足與輪足](docs/legged.md)")
    out.append("- [追蹤的實驗室](docs/labs.md)")
    out.append("- [封存區](docs/archive.md)\n")
    out.append(f"## 本月趨勢（{digests[0].stem}）\n\n{trend}\n")
    out += [f"{s}\n" for _, n, s in sections if n not in PAGES]
    out.append("## 月報\n")
    out += [f"- [{d.stem}](digests/{d.name})" for d in digests]

    (ROOT / "README.md").write_text("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
