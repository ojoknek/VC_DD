#!/usr/bin/env python3
"""
案件ルート内の 業務整理用 から dd materials へ、対応表に従ってファイルをコピーする。
- PDF → ページごとに PNG に変換して配置
- XLSX/XLS → シートごとに CSV に変換して配置
- 上記以外 → そのままコピー
元ファイルは 業務整理用 に残す。

使い方:
  python program/run_copy.py [案件ルート]
  案件ルート: deals/株式会社ABC など。省略時はリポジトリルート（後方互換）。
"""
from pathlib import Path
import os
import shutil
import sys

# このスクリプトの場所からリポジトリルートを算出（program/ の親）
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
# リポジトリルートから実行しても program 内モジュールを import できるようにする
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))


def get_deal_root() -> Path:
    """案件ルートを取得。引数 > 環境変数 DEAL_ROOT > REPO_ROOT（後方互換）。"""
    if len(sys.argv) >= 2 and sys.argv[1].strip():
        p = Path(sys.argv[1].strip())
        return p if p.is_absolute() else REPO_ROOT / p
    deal = os.environ.get("DEAL_ROOT", "").strip()
    if deal:
        p = Path(deal)
        return p if p.is_absolute() else REPO_ROOT / p
    return REPO_ROOT


DEAL_ROOT = get_deal_root()
SOURCE_ROOT = DEAL_ROOT / "業務整理用"
DEST_ROOT = DEAL_ROOT / "dd materials"

# 対応表（業務整理用フォルダ名 → dd materials 内の相対パス）
COPY_MAP = [
    ("01財務　税務申告表", "financial/税務申告表"),
    ("02財務　月次試算表", "financial/月次試算表"),
    ("03財務　月次資金繰実績・予測表", "financial/月次資金繰実績・予測表"),
    ("04事業計画　今後の事業計画・予測表", "business/今後の事業計画・予測表"),
    ("05株主名簿　株主名簿", "round table/株主名簿"),
    ("06資本政策　資本政策", "round table/資本政策表"),
    ("07事業計画　ピッチ資料（事業計画）", "pitch slide"),
    ("08組織　組織図", "corporate/組織図"),
    ("09組織　経営陣プロフィール", "corporate/経営陣プロフィール"),
    ("10知財　特許リスト", "contract/特許リスト"),
    ("11契約書　当ラウンドのタームシート", "round table/当ラウンドのタームシート"),
    ("12契約書　過去の投資契約・株主間契約", "round table/過去の投資契約・株主間契約"),
    ("13登記簿　履歴事項全部証明書", "contract/履歴事項全部証明書"),
    ("14組織図　主な退職者及び退職理由", "corporate/主な退職者及び退職理由"),
    ("15契約書　顧客との契約書", "contract/顧客との契約書"),
    ("16契約書　代理店契約書", "contract/代理店契約書"),
    ("17契約書　政府補助金契約書", "contract/政府補助金契約書"),
    ("18契約書　負債に関する契約", "contract/負債に関する契約"),
    ("19契約書　営業資料", "business/営業資料"),
]


def convert_pdf_to_png(pdf_path: Path, out_dir: Path) -> list[Path]:
    """PDF を PNG 群に変換。convert_pdf_to_png モジュールを使用。"""
    from convert_pdf_to_png import pdf_to_pngs
    return pdf_to_pngs(pdf_path, out_dir)


def convert_xlsx_to_csv(xlsx_path: Path, out_dir: Path) -> list[Path]:
    """XLSX を CSV に変換。convert_xlsx_to_csv モジュールを使用。"""
    from convert_xlsx_to_csv import xlsx_to_csv as _xlsx_to_csv
    return _xlsx_to_csv(xlsx_path, out_dir)


def process_file(src_path: Path, dest_dir: Path) -> None:
    """1 ファイルを変換またはコピーして dest_dir に配置する。"""
    dest_dir.mkdir(parents=True, exist_ok=True)
    suffix = src_path.suffix.lower()

    if suffix == ".pdf":
        convert_pdf_to_png(src_path, dest_dir)
        print(f"  PDF→PNG: {src_path.name} -> {dest_dir}")
    elif suffix in (".xlsx", ".xls"):
        convert_xlsx_to_csv(src_path, dest_dir)
        print(f"  XLSX→CSV: {src_path.name} -> {dest_dir}")
    else:
        dest_file = dest_dir / src_path.name
        shutil.copy2(src_path, dest_file)
        print(f"  コピー: {src_path.name} -> {dest_dir}")


def run_copy() -> None:
    """対応表に従い 業務整理用 から dd materials へコピー（変換あり）。"""
    if not SOURCE_ROOT.is_dir():
        print(f"ソースが見つかりません: {SOURCE_ROOT}", file=sys.stderr)
        print(f"案件ルート: {DEAL_ROOT}", file=sys.stderr)
        sys.exit(1)
    if DEAL_ROOT != REPO_ROOT:
        print(f"案件ルート: {DEAL_ROOT}")

    for src_folder_name, dest_rel in COPY_MAP:
        src_dir = SOURCE_ROOT / src_folder_name
        if not src_dir.is_dir():
            continue
        dest_dir = DEST_ROOT / dest_rel
        print(f"[{src_folder_name}] -> {dest_rel}")
        for f in src_dir.iterdir():
            if f.is_file() and not f.name.startswith("."):
                try:
                    process_file(f, dest_dir)
                except Exception as e:
                    print(f"  エラー: {f.name}: {e}", file=sys.stderr)
    print("完了.")


if __name__ == "__main__":
    run_copy()
